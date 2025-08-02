import React, { useMemo } from 'react';

const MyComponent = () => {
    const staticOptions = useMemo(()=>{
        const options = [
            {id:1, label:'옵션 A'},
            {id:2, label:'옵션 B'},
            {id:3, label:'옵션 C'},
        ]
        return options
    }, [])
  return (
    <div>
      <h2>정적 옵션 목록</h2>
      <ul>
        {staticOptions.map(option=>(<li key={option.id}>{option.label}</li>))}
      </ul>
    </div>
  );
}

export default MyComponent;
