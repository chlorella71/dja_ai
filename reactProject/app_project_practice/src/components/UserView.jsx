import React, {useState, useEffect} from 'react'
import axios from 'axios'

const UserView = () => {

    const [data, setData] = useState(null)
    useEffect(() => {
        const fetch = async () => {
            try {
                const response = await axios.get("http://localhost:3001/users")
                setData(response.data)
                console.log(response.data)
            } catch (err) {
                console.err(err)
            }
        }
        fetch();
    }, [])

    // tableHeader
    const tableHeaders = <tr>{data[0] && Object.keys(data[0]).map((key) => 
        <th key={key}>{key}</th>)}</tr>

    // tableBody
    const tableBody= data?.map((item) => (
        <tr key={item.id}>
            <td>{item.name}</td>
            <td>{item.age}</td>
            <td>{item.email}</td>
            <td>{item.city}</td>
        </tr>
    ))


  return (
    <>
        <table border={1}>
            <thead>{tableHeaders}</thead>
            <tbody>{tableBody}</tbody>
        </table>
      
    </>
  )
}

export default UserView
