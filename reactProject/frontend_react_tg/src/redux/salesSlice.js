import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

// Action
export const salesAction = createAsyncThunk(
    "salesAction", 
    async (_, thunkAPI) => {
        try{
            const response = await axios.get("http://localhost:3001/판매");
            return response.data
        }catch(error){
            return thunkAPI.rejectWithValue(error.message);
        }
    }
)

const salesSlice = createSlice({
    name: "sales",
    initialState: {
        data: [],
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
            .addCase(salesAction.pending, (state) => {
                state.status = 'loading';
            })
            .addCase(salesAction.fulfilled, (state, action) =>{
                state.status = "success";
                state.data = action.payload;
            })
            .addCase(salesAction.rejected, (state, action)=>{
                state.status = "failure";
                state.error = action.payload
            })
    }
})

export const {clearFunction} = salesSlice.actions;
export default salesSlice.reducer