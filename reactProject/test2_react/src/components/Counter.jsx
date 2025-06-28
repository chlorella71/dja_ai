import React from 'react'
import {useDispatch, useSelector} from 'react-redux'

const Counter = () => {
    const {number} = useSelector(state=>state.count)
    const dispatch = useDispatch()
  return (
    <>
        <div>{number}</div>
        <button onClick={()=>dispatch({type:"INCREASE"})}>+</button>
        <button onClick={()=>dispatch({type:"DECREASE"})}>-</button>
    </>
  )
}

export default Counter
