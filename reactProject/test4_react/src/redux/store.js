// import { combineReducers } from "redux";
// import { applyMiddleware, legacy_createStore } from "redux";
// import count from './reducerSlices/countSlice';
// import { thunk } from "redux-thunk";

// const rootReducers = combineReducers({
//     count,
// })

// const store = legacy_createStore(rootReducers, applyMiddleware(thunk));

// export default store;

import { configureStore } from "@reduxjs/toolkit";
import count from "./reducerSlices/countSlice";
import nickname from './reducerSlices/nicknameSlice'
import users from './reducerSlices/userSlice'
import userPost from './reducerSlices/userPostSlice'
import products from './reducerSlices/productSlice'
import productPost from './reducerSlices/productPostSlice'

const store = configureStore({
    reducer: {
        count,
        nickname,
        users,
        userPost,
        products,
        productPost,
    }
});

export default store;