import React, {useState, useReducer} from 'react'
import {useDispatch, useSelector} from 'react-redux'
import { increase, decrease } from '../redux/reducer'

// const increase = 'INCREASE'
// const decrease = 'DECREASE'

// const initialNumber = {
//     number: 0,
// }

// const reducer = (state, action) => {
//     switch(action.type) {
//         case increase:
//             return {...state, number: state.number + 1}
//         case decrease:
//             return {...state, number: state.number - 1}
//         default:
//             return state
//     }
// }

const Reducer = () => {
    // const [state, dispatch] = useReducer(reducer, initialNumber); 

    const dispatch = useDispatch();
    // const state = useSelector(state => {
    //     console.log("state", state)
    //     return state.reducer}
    // )
    const state = useSelector(state =>state.reducer)

    const handlePlusClick = () => {
        dispatch(increase())
    }

    const handleMinusClick = () => {
        dispatch(decrease())
    }


  return (
    <>
      <h3>Reducer</h3><br />

      <div>{state.number}</div>
      <button onClick={handlePlusClick}>+</button>
      <button onClick={handleMinusClick}>-</button>
    </>
  )
}

export default Reducer
