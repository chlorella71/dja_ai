import React, {useState} from 'react'

const initialData = { name: null, age: null, email: null, city: null}

const Form = ({getObj}) => {
    const [obj, setObj] = useState(initialData);

    const handleChange=(event)=>{
        setObj(prev => ({...prev, [event.target.name] : event.target.value}))
    }

    const handleSubmit=(event)=>{
        event.preventDefault()
        getObj(obj)
    }

  return (
    <>
    <h2>정보입력</h2>
    <form onSubmit={handleSubmit}>
        <label htmlFor='name'>이름</label>
        <input type="text" name="name" onChange={handleChange}/>
        <label htmlFor='age'>나이</label>
        <input type="number" name="age" onChange={handleChange}/>
        <label htmlFor='email'>이메일</label>
        <input type="email" name="email" onChange={handleChange}/>
        <label htmlFor='city'>도시</label>
        <input type="text" name="city" onChange={handleChange}/>
        <button type="submit">제출</button>
    </form>
      
    </>
  )
}

export default Form
