import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

// Action
export const categoryAction = createAsyncThunk(
    "categoryAction", 
    async (_, thunkAPI) => {
        try{
            const response = await axios.get("http://localhost:3001/분류");
            return response.data
        }catch(error){
            return thunkAPI.rejectWithValue(error.message);
        }
    }
)

const categorySlice = createSlice({
    name: "category",
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
            .addCase(categoryAction.pending, (state) => {
                state.status = 'loading';
            })
            .addCase(categoryAction.fulfilled, (state, action) =>{
                state.status = "success";
                state.data = action.payload;
            })
            .addCase(categoryAction.rejected, (state, action)=>{
                state.status = "failure";
                state.error = action.payload
            })
    }
})

export const {clearFunction} = categorySlice.actions;
export default categorySlice.reducer