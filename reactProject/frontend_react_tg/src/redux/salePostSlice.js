import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

// Action
export const salePostAction = createAsyncThunk(
    "salePostAction", 
    async (data, thunkAPI) => {
        try{
            const response = await axios.post("http://localhost:3001/판매", data);
            return response.data
        }catch(error){
            return thunkAPI.rejectWithValue(error.message);
        }
    }
)

const salePostSlice = createSlice({
    name: "salePost",
    initialState: {
        data: null,
        status: 'idle',  // loading, success, failure
        error: null
    }, 
    reducers: {
        clearFunction(state){
            state.data = []
            state.status = 'idle'
            state.error = null
        },
    },
    extraReducers: (builder) =>{
        builder
            .addCase(salePostAction.pending, (state) => {
                state.status = 'loading';
            })
            .addCase(salePostAction.fulfilled, (state, action) =>{
                state.status = "success";
                state.data = action.payload;
            })
            .addCase(salePostAction.rejected, (state, action)=>{
                state.status = "failure";
                state.error = action.payload
            })
    }
})

export const {clearFunction} = salePostSlice.actions;
export default salePostSlice.reducer