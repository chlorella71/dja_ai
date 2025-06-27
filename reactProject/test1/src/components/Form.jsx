import React, { useState } from 'react'
import axios from 'axios';

const initialData = {
    name: '',
    age: 0,
    email: null,
    city: ''
}

export const a = 2;

const Form = ({함수}) => {

    const [data, setData] = useState(initialData);

    const handleChange = (e) => {
        setData(prev => (
            {...prev, [e.target.name] : e.target.value}
        ))
    }

    const handleSubmit = (e) => {
        e.preventDefault()
        함수(data)

        const fetch = async () => {
          try {
            const response = await axios.post("http://www.localhost:3001/users",
              data
            )
            console.log(response.data)
            
          } catch (err) {
            console.error(err)
          }
        }
        fetch();
    }

    

  return (
    <>
      <form onSubmit={handleSubmit}>
        <label htmlFor="name">이름:</label><br />
        <input type="text" id="name" name="name" onChange={handleChange} /><br />
        <label htmlFor="age">나이:</label><br />
        <input type="number" id="age" name="age" onChange={handleChange} /><br />
        <label htmlFor="email">이메일:</label><br />
        <input type="email" id="email" name="email" onChange={handleChange} /><br />
        <label htmlFor="city">거주지:</label><br />
        <input type="text" id="city" name="city" onChange={handleChange} /><br />
        <input type="submit" value="제출" /><br />
      </form>
      
    </>
  )
}

export default Form
