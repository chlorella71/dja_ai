import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

// Action
export const regionAction = createAsyncThunk(
    "regionAction", 
    async (_, thunkAPI) => {
        try{
            const response = await axios.get("http://localhost:3001/지역");
            return response.data
        }catch(error){
            return thunkAPI.rejectWithValue(error.message);
        }
    }
)

const regionSlice = createSlice({
    name: "region",
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
            .addCase(regionAction.pending, (state) => {
                state.status = 'loading';
            })
            .addCase(regionAction.fulfilled, (state, action) =>{
                state.status = "success";
                state.data = action.payload;
            })
            .addCase(regionAction.rejected, (state, action)=>{
                state.status = "failure";
                state.error = action.payload
            })
    }
})

export const {clearFunction} = regionSlice.actions;
export default regionSlice.reducer