import React, { useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { fetchGet, fetchPost } from '../redux/reducers/userReducer.js'
import { useEffect } from 'react'

const initialState = {
    name : null,
    age : null,
    email : null,
    city : null,
}

const Users = () => {
    const [userObj, setUserObj] = useState(initialState);
    const state = useSelector(state => state.users)
    const dispatch = useDispatch()

    useEffect(() =>{
        dispatch(fetchGet());
    }, [dispatch])

    const handleChange = (e) => {
        setUserObj(prev=>({...prev,
            [e.target.name] : e.target.value}))   // 변수를 key값으로 사용하고 싶을때 [] 이용   
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        // const object = {
        //     "name": "Peter",
        //     "age": 35,
        //     "email": "Peter@example.com",
        //     "city": "Seoul"
        // }
        await dispatch(fetchPost(userObj))
        dispatch(fetchGet())
    }

    const thead = state.data.length > 0
        ? <tr>{Object.keys(state.data[0])
            .map((key)=>(
                <th key={key}>{key}</th>))}</tr>
        : null

    const tbody = Array.isArray(state.data)
        ? state.data.map((user, index) => {
            return (
                <tr key={index}>
                    {Object.values(user).map((value, i) => (
                        <td key={i}>{value}</td>
                    ))}
                </tr>
            )})
        : null
         

  return (
    <>
        <h2>Users</h2>
        <table>
            <thead>
                {thead}
            </thead>
            <tbody>
                {tbody}
            </tbody>
        </table>
      {/* <div>{state.data && state.data.length > 0 && state.data[0].name}</div><br /> */}
      <form onSubmit={handleSubmit}>
        <label>이름</label>
        <input type="text" name="name" onChange={handleChange} />
        <label>나이</label>
        <input type="number" name="age" onChange={handleChange} />
        <label>이메일</label>
        <input type="email" name="email" onChange={handleChange} />
        <label>도시</label>
        {/* <input type="text" name="city" onChange={handleChange} /> */}
        <select name="city" onChange={handleChange}>
            <option value="">--도시 선택--</option>
            <option value="Seoul">서울</option>
            <option value="Gyeonggi">경기</option>
            <option value="Busan">부산</option>
        </select>
        <button type="submit">제출</button>
      </form>
      {/* <button onClick={handleClick}>제출</button> */}
    </>
  )
}

export default Users
