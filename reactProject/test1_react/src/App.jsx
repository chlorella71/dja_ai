import { useState } from 'react'
import './App.css'
import Table from './components/Table'
import Form from './components/Form'

function App() {
  const [obj, setObj] = useState(null)
  const getObj=(newObj)=>{
    setObj(newObj)
  }

  return (
    <>
      <Form getObj={getObj}/>
      <Table obj={obj}/>
      
    </>
  )
}

export default App
