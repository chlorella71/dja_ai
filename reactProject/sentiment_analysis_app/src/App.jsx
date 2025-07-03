import { useState } from 'react'
import './App.css'
import Sentiment from './components/Sentiment'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Sentiment />
    </>
  )
}

export default App
