import React, {useEffect, useState} from 'react'
import axios from 'axios'

const Fetch = () => {

    const [data, setData] = useState([])
    
    useEffect(() => {

        

        const fetch = async () => {
            try {
                const response = await axios.get("http://localhost:3001/products")
                setData(response.data)
                console.log("response: ", response)
            } catch (err) {
                console.error(err)
            }
        }

        fetch()
    }, [])

  return (
    <div>
        <table border={1}>
            <thead>
                <tr>
                    {data[0] && Object.keys(data[0]).map(key => (
                        <th>{key}</th>
                    ))}
                </tr>
            </thead>
            <tbody>
                {data && data.map(item => {
                    return (
                        <tr>
                            <td>{item.id}</td>
                            <td>{item.name}</td>
                            <td>{item.price}</td>
                            <td>{item.category}</td>
                            <td>{item.inStock ? "O" : "X"}</td>                         
                        </tr>
                    )
                })}
                <tr>
                    <td></td>
                </tr>
            </tbody>
        </table>
      
    </div>
  )
}

export default Fetch
