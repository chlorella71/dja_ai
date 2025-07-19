import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";


// API 기본 URL을 상수로 정의하여 관리의 용이성을 높입니다.
// 실제 배포 환경에서는 환경 변수를 사용하는 것이 일반적입니다.
const API_BASE_URL = "http://localhost:3001"; 

export const register = createAsyncThunk(
  "auth/register",
  async (userData, thunkAPI) => { // 'obj' 대신 'userData'와 같이 명확한 인자 이름을 사용합니다.
    try {
      // ✅ API 엔드포인트를 명확하고 RESTful 하게 변경합니다.
      // '사용자' 대신 'users' 또는 'auth/register'와 같이 영문 복수형을 사용합니다.
      const response = await axios.post(`${API_BASE_URL}/사용자`, userData); 
      
      // ✅ 서버 응답에서 필요한 데이터를 반환합니다.
      // 일반적으로 등록 성공 시 사용자 정보 등을 반환합니다.
      return response.data; 

    } catch (error) {
      // ✅ 에러 응답 구조에 따라 적절한 에러 메시지를 추출합니다.
      // error.response는 Axios 에러에서 서버 응답을 포함합니다.
      const message = 
        (error.response && 
         error.response.data && 
         error.response.data.message) || 
        error.message || 
        error.toString();

      // ✅ rejectWithValue를 사용하여 에러 메시지를 payload로 전달합니다.
      return thunkAPI.rejectWithValue(message);
    }
  }
);

export const login = createAsyncThunk(
  "auth/login",
  async (obj, thunkAPI) => {
    try {
      const response = await axios.get(`${API_BASE_URL}/사용자/?name=${obj.name}`);
      const data = response.data;
      if (data.length === 0) {
        return thunkAPI.rejectWithValue("사용자를 찾을 수 없습니다.");
      }
      const user = data[0];
      if (user.password !== obj.password.toString()) {
        return thunkAPI.rejectWithValue("비밀번호가 틀렸습니다.");
      }
      return user;
    } catch (error) {
      return thunkAPI.rejectWithValue("서버 오류가 발생했습니다.");
    }
  }
);

const initialUser = JSON.parse(localStorage.getItem("user"));

const authSlice = createSlice({
  name: "authSlice",
  initialState: {
    status: "idle",
    user: initialUser,
    isAuthenticated: !!initialUser,
    error: null,
  },
  reducers: {
    logout(state) {
      state.isAuthenticated = false;
      state.user = null;
      state.status = "idle";
      state.error = null;
      localStorage.removeItem("user");
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(login.pending, (state) => {
        state.status = "loading";
        state.error = null;
      })
      .addCase(login.fulfilled, (state, action) => {
        state.status = "succeeded";
        state.isAuthenticated = true;
        state.user = action.payload;
        localStorage.setItem("user", JSON.stringify(action.payload));
      })
      .addCase(login.rejected, (state, action) => {
        state.status = "failed";
        state.error = action.payload;
      });
  },
});

export const { logout } = authSlice.actions;
export default authSlice.reducer;
