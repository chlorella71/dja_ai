import { createSlice } from "@reduxjs/toolkit";
const countSlice = createSlice(
    {
        name: "countSlice", 
        initialState: {
            value: 0,
        },
        reducers:{
            increase: (state) => {state.value += 1},
            decrease: (state) => {state.value -= 1}
        }
    }
)

export const { increase, decrease } = countSlice.actions;
export default countSlice.reducer;