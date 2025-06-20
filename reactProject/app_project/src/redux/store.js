import { legacy_createStore, applyMiddleware, combineReducers } from "redux";
import {thunk} from 'redux-thunk';
import viewReducer from "./reducer";

const rootReducer = combineReducers({
    view: viewReducer,
})


const store = legacy_createStore(rootReducer, applyMiddleware(thunk));

export default store;