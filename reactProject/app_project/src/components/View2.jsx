import axios from 'axios';
import React, { useEffect, useState, useReducer, useLocation } from 'react';
import { useDispatch, useSelector} from 'react-redux'
import { fetchData} from '../redux/reducer'

// 데이터로부터 <tr><td>...</td></tr> 요소 생성
const extractData = (data) => {
    return  Array.isArray(data) && data.map((datum, idx) => {
        const tdList = Object.entries(datum)
            .filter(([key], index) => key !== 'id') // id 제외
            .map(([key, value], tdIdx) => <td key={tdIdx}>{value}</td>);

        return <tr key={idx}>{tdList}</tr>;
    });
};

const success = "SUCCESS"
const failure = "FAILURE"



const initialViewState = {
    data: [],
    error: null,
};

const viewReducer = (state, action) => {
    switch (action.type) {
        case success:
            return { ...state, data: action.payload.data };
        case failure:
            return { ...state, error: action.payload.error };
        default:
            return state;
    }
};

const View2 = () => {

    const [state, dispatch] = useReducer(viewReducer, initialViewState)

    const fetchData = async () => {
        try {
            const response = await axios.get(`http://localhost:3001/${props}`);
            return dispatch({ type: success, payload: { data: response.data }})
        } catch (error) {
            return dispatch({type: failure, payload: {error}})
        }
    };

    useEffect(() => {
        fetchData()    
    }, []);

    const headers = state.data.length > 0 ? Object.keys(state.data[0]).filter((key) => key !== 'id') : []

    return (
        <>
            <h3>View2</h3>
            <table border="1">
                <thead>
                    <tr>
                        {headers.map((header, idx) => (
                            <th key={idx}>{header}</th>
                        ))}
                    </tr>
                </thead>
                <tbody>
                    {extractData(state.data)}
                </tbody>
            </table>
        </>
    );
};

export default View2;