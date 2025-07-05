import axios from 'axios'
import {createSlice, createAsyncThunk} from '@reduxjs/toolkit'

export const fetchPostProducts = createAsyncThunk(
    'fetchPostProducts',
    async (object) => {
        try {
            const response = await axios.post('http://localhost:3001/products', object)
            return response.data
        } catch (error) {
            return error
        }
    }
)

const productPostSlice = createSlice({
    name: 'productPostSlice',
    initialState: {
        loading: false,
        data: [],
        error : null
    },
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(fetchPostProducts.pending, (state) => {
                state.loading=true
                state.error=null
            })
            .addCase(fetchPostProducts.fulfilled, (state, action) => {
                state.loading=false
                state.data=action.payload
            })
            .addCase(fetchPostProducts.rejected, (state, action) => {
                state.loading=false
                state.error=action.payload || 'ERROR!!! Something went wrong...'
            })
    }
})

export default productPostSlice.reducer