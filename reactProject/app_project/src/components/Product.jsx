import axios from 'axios'
import React, {useState} from 'react'
import {useNavigate} from 'react-router-dom'
import {useDispatch} from 'react-redux'
import { fetchProductPost } from '../redux/reducer'

const Product = ({getProps}) => {

  // const [state, setState] = useState(null)
  const [state, setState] = useState({
    name: '',
    price: 0,
    category: '',
    inStock: false,
})

  const navigate = useNavigate();

  const dispatch = useDispatch();

  const props = "products"
  
  const handleSubmit = (e) => {
    e.preventDefault();

    if (!state?.name || state.name.trim() === '') {
      return alert("상품 이름은 필수입니다.");
    }
    if (!state?.price || isNaN(state.price) || Number(state.price) < 0) {
      return alert("가격은 0 이상의 숫자여야 합니다.");
    }

    if (state?.category && state.category.length > 80) {
      return alert("카테고리는 80자 이내로 입력해주세요.");
    }
    
    dispatch(fetchProductPost(state))
    // const fetch = async () => {
    //   try {
    //     const url = "http://localhost:3001/products";
    //     const response = await axios.post(url, state);
    //     console.log(response)
    //   } catch (err) {
    //     console.error(err);
    //   }
    // }
    // fetch(props);
    getProps(props)
    navigate("/view",{state : {target: "products"}});  
  }

  const handleChange = (event) => {
    const {name, type, value, checked} = event.target
    setState(prev => (
      {...prev, [name] : type === 'checkbox'? checked : value}
    // setState(prev => (
    //   {...prev, [event.target.name] : event.target.value}
    ))
  }

  return (
    <>
      <h3>Product</h3>
      <form onSubmit={handleSubmit}>
        <label htmlFor="name">Name</label>
        <input type="text" name="name" required maxLength={80} onChange={handleChange} /><br />
        <label htmlFor="price">Price</label>
        <input type="number" name="price" required min="0" step="1000" onChange={handleChange} /><br />
        <label htmlFor="category">Category</label>
        <input type="text" name="category" maxLength={80} onChange={handleChange} /><br />
        <label htmlFor="inStock">InStock</label>
        <input type="checkbox" name="inStock" onChange={handleChange} /><br />
        <button type="submit">Submit</button>
      </form>
    </>
  )
}

export default Product
