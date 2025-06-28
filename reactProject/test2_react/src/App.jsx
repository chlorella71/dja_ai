import { useState } from 'react'
import './App.css'
import Test from './components/Test.jsx'
import ChangeColor from './components/ChangeColor'
import Counter from './components/Counter.jsx'
import Users from './components/Users.jsx'
import Products from './components/Products.jsx'

function App() {

  return (
    <>
      <ChangeColor />
      <Test />
      <Counter /><br />
      <Users /><br />
      <Products />
    </>
  )
}

export default App
