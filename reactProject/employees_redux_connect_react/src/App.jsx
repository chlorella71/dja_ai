import './App.css'
import Main from './components/Main'
import {Routes, Route} from 'react-router-dom'

function App() {

  return (
    <>
      <Routes>
        <Route path="/" element={<Main/>}/>
      </Routes>
      
    </>
  )
}

export default App;
