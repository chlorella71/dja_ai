import React, {useState} from 'react'
import axios from 'axios'


const initialData = {
    name: null,
    price: null,
    category: null,
    inStock: null

}

const Form = () => {

const [data, setData] = useState(initialData)

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
      data)
      console.log(response.data)
    } catch(err) {
      console.error(err)
    }
  }
}



  return (
    <>
      <form onSubmit={handleSubmit}>
        <label htmlFor="name">name:</label><br />
        <input type="text" id="name" name="name" onChange={handleChange} /><br />
        <label htmlFor="price">price:</label><br />
        <input type="number" id="price" name="price" onChange={handleChange}/><br />
        <label htmlFor="name">category:</label><br />
        <input type="text" id="category" name="category" onChange={handleChange}/><br />
        <label htmlFor="name">inStock:</label><br />
        <input type="text" id="inStock" name="inStock" onChange={handleChange}/><br />
        <button 
      </form>
    </>
  )
}

export default Form
