import React, { useEffect, useRef } from 'react';

const FocusInput = () => {
    const inputRef=useRef(null)
    const handleFocusClick=()=>{
        if(inputRef.current) {
            inputRef.current.focus()
        }
    }
    const handleChangePlacehodler=()=>{
        if(inputRef.current) {
            inputRef.current.placeholder='new placeholder'
        }
    }
    useEffect(()=>{
        console.log(inputRef.current)
    }, [])
  return (
    <div>
        <h2>FocusInput</h2>
      <input type='text' ref={inputRef} placeholder='여기에 입력하세요' />
      <button onClick={handleFocusClick}>focus to input</button>
      <button onClick={handleChangePlacehodler}>change placeholder</button>
    </div>
  );
}

export default FocusInput;
