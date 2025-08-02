import React, { useEffect, useRef } from 'react';

const ValueTracker = ({value}) => {
    const preValueRef = useRef()
    useEffect(()=>{
        preValueRef.current = value
    },[value])
    const preValue = preValueRef.current
  return (
    <div>
      <p>current value: {value}</p>
      <p>old value: {preValue !== undefined ? preValue : '없음'}</p>
      {value !== preValue && preValue !== undefined && (
        <p stype={{color: 'blue'}}>값이 {preValue}에서 {value}로 변경되었습니다.</p>
      )}
    </div>
  );
}

export default ValueTracker;
