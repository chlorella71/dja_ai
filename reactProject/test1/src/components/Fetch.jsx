import axios from 'axios'
import React, { useEffect, useState } from 'react'

const obj = {name:"", age:"", city:""}
Object.keys(obj)

const Fetch = () => {
    const [data, setData] = useState([])

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
        

        {data[0] && data[0].name}
    </>
  )
}

export default Fetch
