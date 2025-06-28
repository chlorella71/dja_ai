import { legacy_createStore } from 'redux';

// 빈 reducer (필수로 하나는 있어야 함)
const dummyReducer = (state = {}, action) => state;

// 빈 store 생성
const store = legacy_createStore(dummyReducer);

export default store;