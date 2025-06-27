import { useState } from 'react'
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'
import './App.css'
import PageA from './components/PageA'
import PageB from './components/PageB'
import PageC from './components/PageC'
import Info from './components/Info'
import Table from './components/Table'

function App() {

  return (
    <>

      <Router>
        <nav>
          <ul>
            <li><Link to="/pageA">pageA</Link></li>
            <li><Link to="/pageB">pageB</Link></li>
            <li><Link to="/pageC">pageC</Link></li>
            <li><Link to="/table">table</Link></li>
            <li><Link to="/info">info</Link></li>
          </ul>
        </nav>
        <Routes>
          <Route path='/pageA' element={<PageA />} />
          <Route path='/pageB' element={<PageB />} />
          <Route path='/pageC' element={<PageC />} />
          <Route path='/info' element={<Info />} />
          <Route path='/table' element={<Table />} />
        </Routes>
      </Router>
    </>
  )
}

export default App
