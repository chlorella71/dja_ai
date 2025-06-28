import axios from 'axios'

export const fetchGet = () => {
    return async (dispatch) => {
        try {
            const response = await axios.get("http://localhost:3001/products")
            dispatch({type: "PRODUCT_SUCCESS", payload: response.data})
            return response.data
        } catch(error) {
            console.log(error)
            dispatch({type:"PRODUCT_FAILURE", error})
        }
    }
}

export const fetchPost = (object) => {
    return async (dispatch) => {
        try {
            const response = await axios.post("http://localhost:3001/products", object)
            dispatch({type: "PRODUCT_SUCCESS", payload: response.data})
            console.log(response.data)
            return response.data
        } catch(error) {
            console.log(error)
            dispatch({type:"PRODUCT_FAILURE", error})
        }
    }
}

const initialState = {
    data: [],
    error: null,
}

const productReducer = (state= initialState, action) => {
    switch(action.type) {
        case "PRODUCT_SUCCESS":
            return {...state, data: action.payload}
        case "PRODUCT_FAILURE":
            return {...state, error: action.error}
        default:
            return state
    }
}

export default productReducer