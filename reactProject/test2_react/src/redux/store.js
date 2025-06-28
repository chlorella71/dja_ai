import { legacy_createStore, combineReducers, applyMiddleware } from "redux";
import colorReducer from "./reducers/colorReducer";
// import { configureStore } from "@reduxjs/toolkit"
import countReducer from "./reducers/countReducer";
import userReducer from "./reducers/userReducer";
import { thunk}  from "redux-thunk"
import productReducer from "./reducers/productReducer";

const rootReducer = combineReducers({
    color : colorReducer, // color : {colorReducer : colorReducer}? // 받을때 color로 받음
    count : countReducer,
    users : userReducer,
    products : productReducer
})

const store = legacy_createStore(rootReducer, applyMiddleware(thunk))

// const store = configureStore({
//     reducer: {
//         color : colorReducer, // color : {colorReducer : colorReducer}? // 받을때 color로 받음
//         count : countReducer,
//         users : userReducer
//     }
// })

export default store