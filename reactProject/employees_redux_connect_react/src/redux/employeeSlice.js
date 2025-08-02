import { createSlice } from "@reduxjs/toolkit"
import { act } from "react";




const initialState = {
    infos: [
        {name: "John", age: 35, job: "frontend", language: "react", pay: 400},
        {name: "Peter", age: 28, job: "backend", language: "java", pay: 300},
        {name: "Sue", age: 38, job: "publisher", language: "javascript", pay: 400},
        {name: "Susan", age: 45, job: "pm", language: "python", pay: 500},
    ],
    upInfo:{},
    mode: '', 
    name: '',
}

const employeeSlice = createSlice({
    name: "employeeSlice",
    initialState,
    reducers:{
        handleSearchName:(state, action) =>{
                  state.name = action.payload;
                  state.upInfo = state.infos
                                .filter(info=>info.name===action.payload)[0]
        },
        handleRegister: (state, action) =>{
            state.infos = [...state.infos, action.payload]
            state.name = action.payload.name
            state.upInfo = action.payload
        },
        
        handleUpgrade:(state, action) => {
                state.infos = state.infos.map(info=>
                    (info.name===action.payload.name ? action.payload: info)
                );
        }, 
        handleDelete: (state)=>{
             state.infos = state.infos
                           .filter(info=>info.name !== state.name);
             state.name = '';
             state.upInfo = {};
             state.mode = '';
        },
        changeMode: (state, action) =>{
            state.mode = action.payload;
        },
        resetState: (state)=>{
            state.infos = [...initialState.infos];
            state.upInfo = {};
            state.name = '';
            state.mode = '';
        }

    },
    // extraReducers:{}
});

export const {
    handleDelete, 
    handleRegister, 
    handleSearchName, 
    handleUpgrade, 
    changeMode,
    resetState,
} = employeeSlice.actions;

export default employeeSlice.reducer;