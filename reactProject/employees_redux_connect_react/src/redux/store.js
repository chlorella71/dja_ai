import { configureStore } from "@reduxjs/toolkit";
import employee from './employeeSlice';


const store = configureStore({
    reducer:{
        employee,
    }
})

export default store;