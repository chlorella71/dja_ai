import React, { useState } from 'react'
import { useDispatch } from 'react-redux'
import { fetchPostUsers} from '../redux/reducerSlices/userPostSlice'
import { fetchUsers} from '../redux/reducerSlices/userSlice'
import Modal from '../components/Modal'

// userData = { "id": 1, "name": "Alice", "age": 30, "email": "alice@example.com", "city": "New York" },


const UserPost = () => {
  const [user, setUser] = useState({
    name: '',
    age: '',
    email: '',
    city: '',
  });

  const [modal, setModal] = useState()

  const dispatch = useDispatch();

  const handleChange = (e) => {
    setUser(prev=>({
      ...prev, [e.target.name] : e.target.value
    }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      await dispatch(fetchPostUsers(user)).unwrap()
      dispatch(fetchUsers())
      setUser({
        name: '',
        age: '',
        email: '',
        city: '',
      })
      setModal('유저등록성공!')
      setTimeout(()=>setModal(null), 1000)
    } catch (error) {
      console.error('에러: ', error);
      setModal('등록 실패!...')
      setTimeout(()=>setModal(null), 1000)
    }

  }

  return (
    <>
      <div><h2>Userpost</h2></div>
      <form onSubmit={handleSubmit}>
        <input type="text" name="name" placeholder='이름' value={user.name}onChange={handleChange}/>
        <input type="number" name="age" placeholder='나이' value={user.age} onChange={handleChange} />
        <input type="email" name="email" placeholder='이메일' value={user.email} onChange={handleChange} />
        <input type="text" name="city" placeholder='도시' value={user.city} onChange={handleChange} />
        <button type="submit">등록</button>
      </form>
      <div>{modal && <Modal message={modal} />}</ div>
    </>
  )
}

export default UserPost
