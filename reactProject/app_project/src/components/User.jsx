import React, {useState} from 'react'
import axios from 'axios'
import {useNavigate} from 'react-router-dom'
import {useDispatch} from 'react-redux'
import {fetchUserPost} from '../redux/reducer'

const User = ({getProps}) => {

  const [obj, setObj] = useState(null);
  // const [obj, setObj] = useState({});

  const navigate = useNavigate();

  const dispatch = useDispatch()

  const props = "users"

  const handleChange = (e) => {
    setObj(prev => (
      {...prev, [e.target.name]: e.target.value}
    ))
  }

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!obj?.name || obj.name.trim() === '') {
      return alert("이름은 필수입니다.");
    }
    if (!obj?.age || isNaN(obj.age) || Number(obj.age) < 0) {
      return alert("유효한 나이를 입력해주세요.");
    }
    if (!obj?.email || !/\S+@\S+\.\S+/ .test(obj.email)) {
      return alert("유효한 이메일을 입력해주세요.");
    }

    dispatch(fetchUserPost(obj))
    // const fetch = async () => {
    //     try {
    //         const url = "http://localhost:3001/users";
    //         const response = await axios.post(url, obj);
    //         console.log(response)
    //     } catch (err) {
    //         console.error(err);
    //     }
    // };
    // fetch(props);
    getProps(props)
    navigate("/view",{state : {target: "users"}});  
  }

  return (
    <div>
      <h3>User</h3>
      <form onSubmit={handleSubmit}>
        <label htmlFor="name">Name</label>
        <input type='text' name='name' onChange={handleChange} required/><br />
        <label htmlFor="age">Age</label>
        <input type='number' name='age' onChange={handleChange} required/><br />
        <label htmlFor="email">Email</label>
        <input type='email' name='email' onChange={handleChange} required/><br />
        <label htmlFor="city">City</label>
        <input type='text' name='city' onChange={handleChange} required/><br />
        <button type='submit'>Submit</button>
      </form>
    </div>
  )
}

export default User
