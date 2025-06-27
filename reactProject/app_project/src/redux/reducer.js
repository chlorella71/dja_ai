import axios from 'axios';

// export const FETCH_DATA_REQUEST = 'FETCH_DATA_REQUEST';
// export const FETCH_DATA_SUCCESS = 'FETCH_DATA_SUCCESS';
// export const FETCH_DATA_FAILURE = 'FETCH_DATA_FAILURE';

export const fetchData = (target) => async (dispatch) => {
    dispatch({ type: "LOADING" });

    try {
        const response = await axios.get(`http://localhost:8000/${target}/`);
        dispatch({ type: "SUCCESS", payload: response.data });
    } catch (error) {
        dispatch({ type: "FAILURE", error });
    }
};


export const fetchUserPost = (obj) => async (dispatch) => {
    try {
        const url = "http://localhost:8000/users/"
        const response = await axios.post(url, obj)
        dispatch({type: "SUCCESS", data: response.data})
    } catch (error) {
        dispatch({type:"FAILURE", error})
}}

export const fetchProductPost = (obj) => async (dispatch) => {
    try {
        const url = "http://localhost:8000/products/"
        const response = await axios.post(url, obj)
        dispatch({type: "SUCCESS", data: response.data})
    } catch (error) {
        dispatch({type:"FAILURE", error})
}}

// const fetch = async () => {
//       try {
//         const url = "http://localhost:3001/products";
//         const response = await axios.post(url, state);
//         console.log(response)
//       } catch (err) {
//         console.error(err);
//       }
//     }
//     fetch(props);

const initialViewState = {
    loading: false,
    data: [],
    error: null,
};

const viewReducer = (state = initialViewState, action) => {
    switch (action.type) {
        case "LOADING":
            return { ...state, loading: true, error: null };
        case "SUCCESS":
            return { ...state, loading: false, data: action.payload };
        case "FAILURE":
            return { ...state, loading: false, error: action.error };
        default:
            return state;
    }
};

export default viewReducer;