import React, {useState,useReducer} from 'react'
import { useSelector, useDispatch } from 'react-redux'

const style = {
    width: "100px",
    height: "100px",
    backgroundColor: "black",
    border: "1px solid black",
    color: "white"
}

// const initialState = {color: 'black'}

// const colorReducer = (state, action) => {
//     switch(action.type) {
//         case "RED":
//             return { ...state, color:"red"}
//         case "BLUE":
//             return { ...state, color:"blue"}
//         case "GREEN":
//             return { ...state, color:"green"}
//         default:
//             return state
//     }
// }

const ChangeColor = () => {
    const state =useSelector(state=>state.color)
    const dispatch = useDispatch()
    // const [state, dispatch] = useReducer(colorReducer, initialState)
    const [color, setColor] = useState("black")
    const [textColor, setTextColor]=useState("white")
    const handleClick=(param)=>{
        setColor(param)
    }
    const handleClick2=(param)=>{
        dispatch({type: param})
        console.log("state", state)
    }


    // const handleClick2 = (param) => {
    //     param === "red" ? dispatch({type: "RED"}) :
    //         param === "blue" ? dispatch({type: "BLUE"}) : dispatch({type: "GREEN"})
    // }

  return (
    <>
        <div style={{...style, backgroundColor: state.color}}>안녕하세용~~~</div>
        <button onClick={()=>handleClick2("RED")}>red2</button>
        <button onClick={()=>handleClick2("BLUE")}>blue2</button>
        <button onClick={()=>handleClick2("GREEN")}>green2</button><br />
        <div style={{...style, backgroundColor: color, width: color, color: textColor}}>안녕하세요!!!</div>
        <button onClick={()=>handleClick("red")}>Red</button>
        <button onClick={()=>handleClick("green")}>Green</button>
        <button onClick={()=>handleClick("blue")}>Blue</button><br />
        <button onClick={()=>setTextColor("red")}>Red</button>
        <button onClick={()=>setTextColor("green")}>Green</button>
        <button onClick={()=>setTextColor("blue")}>Blue</button>
    </>
  )
}

export default ChangeColor
