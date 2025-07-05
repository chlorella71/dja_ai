import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { increase, decrease } from '../redux/reducerSlices/countSlice';

const Count = () => {
    const {value} = useSelector(state=>state.count)
    const dispatch = useDispatch();
  return (
    <div>
        <h2>Count</h2>
        <div>
            {value}
        </div>
        <button onClick={()=>dispatch(increase())}>+</button>
        <button onClick={()=>dispatch(decrease())}>-</button>
    </div>
  )
}

export default Count