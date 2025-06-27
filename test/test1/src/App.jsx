import { useState } from 'react'
import './App.css'



function App() {
  const [num1, setNum1] =useState('')
  const [num2, setNum2] = useState('')
  const [result, setResult] =useState('')

  const cal = (oper) => {
    const a = parseFloat(num1)
    const b = parseFloat(num2)

    if (oper === 'C') {
      setResult('')
      setNum1('')
      setNum2('')
      return
    }

    let res
    switch (oper) {
      case '+':
        res = a + b
        break
      case '-':
        res=a-b
        break
      case '*':
        res=a*b
        break
      case '/':
        res= b !==0? a/b: 'error'
        break
      default:
        res=''
    }
    setResult(res)

  }

  return (
    <>
      <input type="number" name="num1" value={num1} onChange={(e)=> setNum1(e.target.value)}/>
      <input type="number" name="num2" value={num2} onChange={(e)=> setNum2(e.target.value)}/><br />
      <button onClick={() => cal('+')}>+</button>
      <button onClick={() => cal('-')}>-</button>
      <button onClick={() => cal('*')}>*</button>
      <button onClick={() => cal('/')}>/</button>
      <button onClick={() => cal('C')}>C</button><br />
      <input type="number" value={result} readOnly placeholder="result"/>
    </>
  )
}

export default App
