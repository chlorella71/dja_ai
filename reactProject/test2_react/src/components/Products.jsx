import React, { useState } from 'react'
import {useDispatch, useSelector} from 'react-redux'
import {fetchGet, fetchPost} from '../redux/reducers/productReducer.js'
import {useEffect} from 'react'

const initialState = {
    name: null,
    price : null,
    category : null,
    inStock : false,
}

const Products = () => {
    const [product, setProduct] = useState(initialState)
    const state = useSelector(state => state.products)
    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(fetchGet())
    }, [dispatch])

    const thead = state.data.length > 0
        ?<tr>{Object.keys(state.data[0])
            .map((key)=>(
                <th key={key}>{key}</th>))}</tr>
        : null

    const tbody = Array.isArray(state.data)
        ? state.data.map((user, index) => {
            return (
                <tr key={index}>
                    {Object.values(user).map((value, i) => (
                        <td key={i}>
                            {typeof value === 'boolean'
                                ? (value ? "on" : "off")
                                : value}
                        </td>
                    ))}
                </tr>
            )})
        : null

    const handleChange = (e) => {
        const { name, type, value, checked }= e.target
        setProduct(prev=>({...prev,
            [name]:type === "checkbox"? checked: value}))
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        await dispatch(fetchPost(product))
        dispatch(fetchGet())
    }

  return (
    <>
      <h2>Products</h2>
      <table>
        <thead>
            {thead}
        </thead>
        <tbody>
            {tbody}
        </tbody>
      </table>
      <form onSubmit={handleSubmit}>
        <label>품명</label>
        <input type="text" name="name" onChange={handleChange} />
        <label>가격</label>
        <input type="number" name="price" onChange={handleChange} />
        <label>품목</label>
        <input type="text" name="category" onChange={handleChange} />
        <label>재고</label>
        <input type="checkbox" name="inStock" onChange={handleChange} />
        <button type="submit">제출</button>
      </form>
    </>
  )
}

export default Products
