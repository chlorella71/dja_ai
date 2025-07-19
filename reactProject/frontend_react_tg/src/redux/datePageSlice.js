import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

// Action
export const datePageAction = createAsyncThunk(
    "datePageAction", 
    async (_, thunkAPI) => {
        try{
            const response = await axios.get("http://localhost:3001/날짜");
            return response.data
        }catch(error){
            return thunkAPI.rejectWithValue(error.message);
        }
    }
)

const datePageSlice = createSlice({
    name: "datePage",
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
            .addCase(datePageAction.pending, (state) => {
                state.status = 'loading';
            })
            .addCase(datePageAction.fulfilled, (state, action) =>{
                state.status = "success";
                state.data = action.payload;
            })
            .addCase(datePageAction.rejected, (state, action)=>{
                state.status = "failure";
                state.error = action.payload
            })
    }
})

export const {clearFunction} = datePageSlice.actions;
export default datePageSlice.reducer