import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

// Action
export const channelAction = createAsyncThunk(
    "channelAction", 
    async (_, thunkAPI) => {
        try{
            const response = await axios.get("http://localhost:3001/채널");
            return response.data
        }catch(error){
            return thunkAPI.rejectWithValue(error.message);
        }
    }
)

const channelSlice = createSlice({
    name: "channel",
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
            .addCase(channelAction.pending, (state) => {
                state.status = 'loading';
            })
            .addCase(channelAction.fulfilled, (state, action) =>{
                state.status = "success";
                state.data = action.payload;
            })
            .addCase(channelAction.rejected, (state, action)=>{
                state.status = "failure";
                state.error = action.payload
            })
    }
})

export const {clearFunction} = channelSlice.actions;
export default channelSlice.reducer