import { useState } from 'react'
import {Routes, Route, Link } from 'react-router-dom'
import './App.css'
import Page1 from './components/Page1'
import Page2 from './components/Page2'
import Page3 from './components/Page3'
import Home from './components/Home'

function App() {

  return (
    <>
      <style> {`
        nav {
          position: fixed;
          top: 0;
          left: 0;
          width: 100%;
          padding: 10px 20px;
          display: flex;
          gap: 20px;
          justify-content: center;
          align-items: center;
        } `}
      </style>

      <nav>
        <Link to="/">Home</Link>
        <Link to="/page1">Page1</Link>
        <Link to="/page2">Page2</Link>
        <Link to="/page3">Page3</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/page1" element={<Page1 />} />
        <Route path="/page2" element={<Page2 />} />
        <Route path="/page3" element={<Page3 />} />
      </Routes>
    </>
  )
}

export default App
