import Fetch from './components/Fetch'
import './App.css'
import Form from './components/Form'
import { Routes, Route, Link } from 'react-router-dom'

function App() {

  return (
    <>
      <Routes>
        <Route path='/form' element={<Form />}></Route>
        <Route path='/fetch' element={<Fetch />}></Route>
      </Routes>

      <nav>
        <ul>
          <li><Link to="/form">Form</Link></li>
          <li><Link to="/fetch">Fetch</Link></li>
        </ul>
      </nav>

      
    </>
  )
}

export default App
