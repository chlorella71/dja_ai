import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

// Action
export const subcategoryAction = createAsyncThunk(
    "subcategoryAction", 
    async (_, thunkAPI) => {
        try{
            const response = await axios.get("http://localhost:3001/제품분류");
            return response.data
        }catch(error){
            return thunkAPI.rejectWithValue(error.message);
        }
    }
)

const subcategorySlice = createSlice({
    name: "subcategory",
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
            .addCase(subcategoryAction.pending, (state) => {
                state.status = 'loading';
            })
            .addCase(subcategoryAction.fulfilled, (state, action) =>{
                state.status = "success";
                state.data = action.payload;
            })
            .addCase(subcategoryAction.rejected, (state, action)=>{
                state.status = "failure";
                state.error = action.payload
            })
    }
})

export const {clearFunction} = subcategorySlice.actions;
export default subcategorySlice.reducer