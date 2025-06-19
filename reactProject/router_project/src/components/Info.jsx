import React, { useState } from 'react'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const initialData = {
    name: '',
    age: 0,
    email: null,
    city: ''
}

const Info = () => {

const [data, setData] = useState(initialData);

const navigate = useNavigate();

    const handleChange = (e) => {
        setData(prev => (
            {...prev, [e.target.name] : e.target.value}
        ))
    }

    const handleSubmit = (e) => {
        e.preventDefault()

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

        navigate('/table')
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

export default Info
