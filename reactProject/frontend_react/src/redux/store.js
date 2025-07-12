import { configureStore } from "@reduxjs/toolkit";
import auth from './authSlice'


const store =configureStore({
    reducer:{
        // key: "value"
        auth,
    }
})

export default store