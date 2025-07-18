import { Routes, Route } from 'react-router-dom'
import './App.css'
import View from './components/View'
import User from './components/User'
import Product from './components/Product'
import {Link} from 'react-router-dom'
import React, {useState} from 'react'
// import View2 from './components/View2'

function App() {

  const [props, setProps] = useState("");
  const getProps = (props) => {
    setProps(props);
  }

  return (
    <>
      <nav>
        <li><Link to ="/product">Product</Link></li>
        <li><Link to ="/user">User</Link></li>
        {/* <li><Link to ="/view">View</Link></li> */}
        {/* <li><Link to ="/view2">View2</Link></li> */}
      </nav>
      

      <Routes>
        <Route path='/product' element={<Product getProps={getProps}/>} />
        <Route path='/user' element={<User getProps={getProps}/>} />
        <Route path='/view' element={<View />} />
        {/* <Route path='/view2' element={<View2 />} /> */}
      </Routes>
    </>
  )
}

export default App
