import axios from 'axios'
import {createSlice, createAsyncThunk } from "@reduxjs/toolkit"
// createSlice : reducer받는 함수, createAsyncThunk : axios?, fetch? 받는 함수?


export const fetchPostUsers = createAsyncThunk(
    'fetchPostUsers',
    async (object) => { //인자받는곳에 async, 함수받는곳에 await
        try {  // 오류가 발생하면 서버가 다운되므로 try catch로 막음
            const response = await axios.post('http://localhost:3001/users', object)
        return response.data // action.payload
        } catch (error) {
            return error // action.error? action.payload?
        }

    }
)

const userPostSlice = createSlice({
    name: 'userPostSlice',
    initialState: {
        loading: false,
        data: [], // 모르면 null로해도되지만 알면 명시적으로 써주는 것이 좋음 json형태 여러개가 날라오니깐 []형태
        error: null
    },
    reducers: {},
    extraReducers: (builder) => { // 밖에 있는 리듀서, api를 받는 곳?
        builder
            .addCase(fetchPostUsers.pending, (state) => { // promise 형식?, 요청후 응답대기
                state.loading = true
                state.error = null
            })
            .addCase(fetchPostUsers.fulfilled, (state, action) => { // promise 형식?, 데이터송신성공
                state.loading = false
                state.data = action.payload
            })
            .addCase(fetchPostUsers.rejected, (state, action) => { // promise 형식?, 실패, 에러발생
                state.loading = false
                state.error = action.payload || 'ERROR! Something went wrong...'
            })
    }
})


// reducer는 api만 처리
// action은 그 페이지에서 짬
// 지금은 연습하려고 action도 같이 넣어봄

export default userPostSlice.reducer