const initialState = {color: 'black'}

const colorReducer = (state=initialState, action) => {
    switch(action.type) {  // action에서 type이란 key에 접근
        case "RED":
            return { ...state, color:"red"}
        case "BLUE":
            return { ...state, color:"blue"}
        case "GREEN":
            return { ...state, color:"green"}
        default:
            return state
    }
}

export default colorReducer