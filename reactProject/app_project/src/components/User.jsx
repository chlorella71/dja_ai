import React, {useState} from 'react'
import axios from 'axios'
import {useNavigate} from 'react-router-dom'

const User = ({getProps}) => {

  const [obj, setObj] = useState(null);
  // const [obj, setObj] = useState({});

  const navigate = useNavigate();

  const props = "users"

  const handleChange = (e) => {
    setObj(prev => (
      {...prev, [e.target.name]: [e.target.value]}
    ))
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    const fetch = async () => {
        try {
            const url = "http://localhost:3001/users";
            const response = await axios.post(url, obj);
            console.log(response)
        } catch (err) {
            console.error(err);
        }
    };
    fetch(props);
    getProps(props)
    navigate("/view");  
  }

  return (
    <div>
      <h3>User</h3>
      <form onSubmit={handleSubmit}>
        <label htmlFor="name">Name</label>
        <input type='text' name='name' onChange={handleChange} /><br />
        <label htmlFor="age">Age</label>
        <input type='number' name='age' onChange={handleChange} /><br />
        <label htmlFor="email">Email</label>
        <input type='email' name='email' onChange={handleChange} /><br />
        <label htmlFor="city">City</label>
        <input type='text' name='city' onChange={handleChange} /><br />
        <button type='submit'>Submit</button>
      </form>
    </div>
  )
}

export default User
