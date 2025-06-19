import React, {useState, useEffect} from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'


const Table = () => {

    const [data, setData] = useState([]);

    useEffect(() => {
        const fetch = async () => {
            try {
                const response = await axios.get("http://localhost:3001/users")
                setData(response.data)
                console.log("response: ", response)
            } catch (err) {
                console.error(err)
            }
        }

        fetch();
    }, [])

  return (
    <>

        <table border={1}>
            <thead>
                <tr>
                    {data[0] && Object.keys(data[0]).map(key => (
                        <th>{key}</th>
                    ))}
                </tr>
            </thead>
            <tbody>
                {data?.map(item => {
                    return (
                        <tr>
                            <td>{item.id}</td>
                            <td>{item.name}</td>
                            <td>{item.age}</td>
                            <td>{item.email}</td>
                            <td>{item.city}</td>
                        </tr>
                    )
                })}
            </tbody>
        </table>

        <Link to='/info'>등록</Link>
    </>
  )
}

export default Table
