import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

// Action
export const promotionAction = createAsyncThunk(
    "promotionAction", 
    async (_, thunkAPI) => {
        try{
            const response = await axios.get("http://localhost:3001/프로모션");
            return response.data
        }catch(error){
            return thunkAPI.rejectWithValue(error.message);
        }
    }
)

const promotionSlice = createSlice({
    name: "promotion",
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
            .addCase(promotionAction.pending, (state) => {
                state.status = 'loading';
            })
            .addCase(promotionAction.fulfilled, (state, action) =>{
                state.status = "success";
                state.data = action.payload;
            })
            .addCase(promotionAction.rejected, (state, action)=>{
                state.status = "failure";
                state.error = action.payload
            })
    }
})

export const {clearFunction} = promotionSlice.actions;
export default promotionSlice.reducer