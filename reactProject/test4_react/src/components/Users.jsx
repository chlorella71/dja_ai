import React, { useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { fetchUsers} from '../redux/reducerSlices/userSlice'

const Users = () => {
    const {loading, data, error} = useSelector(state=> state.users) // store의 users에 해당
    const dispatch = useDispatch();
    useEffect(()=>{
        dispatch(fetchUsers())
    }, [dispatch])
  return (
    <>
        <div><h2>Users</h2></div>
        {loading && <p>User Data loading...</p>}
        {error && <p>{error}</p>}
        {!loading && data.length === 0 && <p>User Data Not Exist</p>}
        <ul>
            {data.map(user=>(
                <li key={user.id}>
                    <strong>{user.name}</strong> ({user.age}세, {user.city}) - {user.email}
                </li>
            ))}
        </ul>

    </>
  )
}

export default Users
