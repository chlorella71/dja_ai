import axios from "axios"

// Action 함수
export const fetchGet = () => {
    return async (dispatch) => {   // thunk가 작동하는 곳
        try {
            const response = await axios.get("http://localhost:3001/users")
            dispatch({type: "USER_SUCCESS", payload: response.data})
            return response.data       
        } catch(error) {
            console.log(error)
            dispatch({type:"USER_FAILURE", error})  // error : error
        }
        
    }
}

// Action 함수
export const fetchPost = (object) => {
    return async (dispatch) => {   // thunk가 작동하는 곳
        try {
            const response = await axios.post("http://localhost:3001/users", object)
            dispatch({type: "USER_SUCCESS", payload: response.data})
            console.log(response.status, response.data)
            return response.data                
        } catch(error) {
            console.log(error)
            dispatch({type:"USER_FAILURE", error})  // error : error
        }
        
    }
}

const initialState = {
    data: [],
    error: null,
}

const userReducer = (state= initialState, action) => {
    switch(action.type) {
        case "USER_SUCCESS":
            return {...state, data: action.payload}
        case "USER_FAILURE":
            return {...state, error: action.error}
        default:
            return state
    }
}

export default userReducer