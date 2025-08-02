import React, { useEffect, useRef, useState } from 'react';

const Timer = () => {
    const [count, setCount] = useState(0)
    const intervalRef = useRef(null)
    useEffect(()=>{
        intervalRef.current=setInterval(()=>{
            setCount(prev=>prev + 1)
        }, 1000)
        return ()=>{
            if (intervalRef.current) {
                clearInterval(intervalRef.current)
            }
        }
    },[])
    const handleStopTimer=()=>{
        if(intervalRef.current) {
            clearInterval(intervalRef.current)
            intervalRef.current= null
        }
    }
  return (
    <div>
      <p>count: {count}</p>
      <button onClick={handleStopTimer}>stop timer</button>
    </div>
  );
}

export default Timer;
