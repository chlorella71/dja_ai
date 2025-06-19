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



  return (
    <>
      <form>
        <label htmlFor="name">name:</label><br />
        <input type="text" id="name" name="name" /><br />
        <label htmlFor="price">price:</label><br />
        <input type="number" id="price" name="price" /><br />
        <label htmlFor="name">category:</label><br />
        <input type="text" id="name" name="name" /><br />
        <label htmlFor="name">inStock:</label><br />
        <input type="text" id="name" name="name" /><br />
      </form>
    </>
  )
}

export default Form
