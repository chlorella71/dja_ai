import axios from 'axios'
import {createSlice, createAsyncThunk} from '@reduxjs/toolkit'

export const fetchProducts = createAsyncThunk(
    'fetchProducts',
    async () => {
        try {
            const response = await axios.get('http://localhost:3001/products')
            return response.data
        } catch (error) {
            return error
        }
    }
)

const productSlice = createSlice({
    name: 'productSlice',
    initialState: {
        loading: false,
        data: [],
        error : null
    },
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(fetchProducts.pending, (state) => {
                state.loading=true
                state.error=null
            })
            .addCase(fetchProducts.fulfilled, (state, action) => {
                state.loading=false
                state.data=action.payload
            })
            .addCase(fetchProducts.rejected, (state, action) => {
                state.loading=false
                state.error=action.payload || 'ERROR!!! Something went wrong...'
            })
    }
})

export default productSlice.reducer