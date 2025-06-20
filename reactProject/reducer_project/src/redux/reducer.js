// action
// export const increase = () => {
//     return (dispatch) => {
//         dispatch({type:"INCREASE"})
//     }
// }

export const increase = () => (dispatch) => {
        dispatch({type:"INCREASE"})
}

export const decrease = () => {
    return (dispatch) => {
        dispatch({type:"DECREASE"})
    }
}

// initialState 상태초기화
const initialNumber = {
    number: 0,
}

// reducer reduce함수
const reducer = (state=initialNumber, action) => {
    switch(action.type) {
        case "INCREASE":
            return {...state, number: state.number + 1}
        case "DECREASE":
            return {...state, number: state.number - 1}
        default:
            return state
    }
}

export default reducer;