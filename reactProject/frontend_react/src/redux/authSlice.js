import { createAsyncThunk, createSlice } from "@reduxjs/toolkit"
import axios from "axios"

const API_BASE_URL = "http://localhost:3001"

const persistedUser= JSON.parse(localStorage.getItem("user"))

// action
export const register = createAsyncThunk(
    "auth/register", // action type prefix
    async (obj, thunkAPI)=> {
        try {
            const response = await axios.post(`${API_BASE_URL}/사용자`, obj) // json server port : 3001
            return response.data // obj
        } catch (error) {
            return thunkAPI.rejectWithValue("회원가입 실패")
        }
    }
)

// action
export const login = createAsyncThunk(
    "auth/login",
    async (obj, thunkAPI)=> {
        const response = await axios.get(`${API_BASE_URL}/사용자/?name=${obj.name}`) // json server port : 3001
        const data = response.data
        if (data.length===0){
            return thunkAPI.rejectWithValue("사용자를 찾을 수 없습니다.")
        }
        const user= data[0]
        if (user.password!==obj.password.toString()){
            return thunkAPI.rejectWithValue("비밀번호가 틀렸습니다.")
        }
        return user
    }
)

const authSlice = createSlice({
    name: "authSlice",
    initialState: {
        status: "idle",
        user: persistedUser || null,
        error: null,
        isAuthenticated: !!persistedUser
    },
    reducers:{
        logout(state) {
            state.isAuthenticated=false
            state.user=null
            state.status="idle"
            state.error= null
            localStorage.removeItem("user")
        }
    },
    extraReducers:(builder)=>{
        builder
            .addCase(login.pending, (state)=> {
                state.status = "loading"
            })
            .addCase(login.fulfilled, (state, action)=> { //fulfilled : 성공
                state.status="succeeded"
                state.isAuthenticated=true
                state.user = action.payload // return user 값
                localStorage.setItem("user", JSON.stringify(action.payload))
            })
            .addCase(login.rejected, (state, action) => {
                state.status="failed"
                state.error = action.payload
            })
    }

})
export const {logout} = authSlice.actions
export default authSlice.reducer