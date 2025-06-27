import { useState } from 'react'
import './App.css'
import { Link, Route, Routes } from 'react-router-dom'

const nav = {
  position: 'fixed',
  top: 0,
  left: 0,
  width: '100%',
  padding: '1rem 0'
  
}

const hov = {
  backgroundColor : '#555',
}

const link = {
  margin: '0 1.5rem'
}

function NavLink({to, text}) {
   const [hover, setHover] = useState(false)

   return (
    <>
      <Link to={to} style={hover? {...link, ...hov }: link} 
        onMouseEnter={()=>setHover(true)}
        onMouseLeave={()=>setHover(false)}>{text}</Link>
    </>
   )
}

function Contact() {
  return (
    <>
      <h2>Contact</h2>
    </>
  )
}

function About() {
  return (
    <>
      <h2>About</h2>
    </>
  )
}

function Home() {
  return (
    <>
      <h2>Home</h2>
    </>
  )
}

function App() {

  return (
    <>
      <nav style={nav}>
        <NavLink to="/home" text="Home" />
        <NavLink to="/about" text="About" />
        <NavLink to="/contact" text="Contact" />
      </nav>

      <Routes>
        <Route path="/home" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </>
  )
}

export default App
