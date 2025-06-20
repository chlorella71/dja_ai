import axios from 'axios'
import React, {useState} from 'react'
import {useNavigate} from 'react-router-dom'

const Product = ({getProps}) => {

  const [state, setState] = useState(null)

  const navigate = useNavigate();

  const props = "products"
  
  const handleSubmit = (e) => {
    e.preventDefault();
    const fetch = async () => {
      try {
        const url = "http://localhost:3001/products";
        const response = await axios.post(url, state);
        console.log(response)
      } catch (err) {
        console.error(err);
      }
    }
    fetch(props);
    getProps(props)
    navigate("/view");
  }

  const handleChange = (event) => {
    setState(prev => (
      {...prev, [event.target.name] : event.target.value}
    ))
  }

  return (
    <>
      <h3>Product</h3>
      <form onSubmit={handleSubmit}>
        <label htmlFor="name">Name</label>
        <input type="text" name="name" onChange={handleChange} /><br />
        <label htmlFor="name">Price</label>
        <input type="number" name="price" onChange={handleChange} /><br />
        <label htmlFor="name">Category</label>
        <input type="text" name="category" onChange={handleChange} /><br />
        <label htmlFor="name">InStock</label>
        <input type="text" name="inStock" onChange={handleChange} /><br />
        <button type="submit">Submit</button>
      </form>
    </>
  )
}

export default Product
