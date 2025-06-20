import axios from 'axios';

export const FETCH_DATA_REQUEST = 'FETCH_DATA_REQUEST';
export const FETCH_DATA_SUCCESS = 'FETCH_DATA_SUCCESS';
export const FETCH_DATA_FAILURE = 'FETCH_DATA_FAILURE';

export const fetchData = (props) => {
    return async (dispatch) => {
        dispatch({ type: FETCH_DATA_REQUEST });

        try {
            const response = await axios.get(`http://localhost:3001/${props}`);
            dispatch({ type: FETCH_DATA_SUCCESS, payload: response.data });
        } catch (error) {
            dispatch({ type: FETCH_DATA_FAILURE, error });
        }
    };
};

const initialViewState = {
    loading: false,
    data: [],
    error: null,
};

const viewReducer = (state = initialViewState, action) => {
    switch (action.type) {
        case FETCH_DATA_REQUEST:
            return { ...state, loading: true, error: null };
        case FETCH_DATA_SUCCESS:
            return { ...state, loading: false, data: action.payload };
        case FETCH_DATA_FAILURE:
            return { ...state, loading: false, error: action.error };
        default:
            return state;
    }
};

export default viewReducer;