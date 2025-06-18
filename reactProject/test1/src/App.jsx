import { useState } from 'react'
import './App.css'
import Child from './components/Child'

const scores = [
  {name: "John", kor: 90, math: 87},
  {name: "Peter", kor: 91, math: 81},
  {name: "Sue", kor: 92, math: 82}
]
// const scores = {name: "John", kor: 90, math: 87}

const tags = [<div>1</div>, <div>2</div>, <div>3</div>]

const extract = () => {
  return scores.filter(item => item.name === 'Peter')
}

const average = () => {
  return scores.reduce((res, item) => {
    return res + item.kor
  }, 0)
}

const App = () => {

  const [data, setData] = useState(scores)
  const [greet, setGreet] = useState(null)
  const getData = (greet) => {
    setGreet(greet);
  }

  const handleClick = () => {
    const newData = data.map(item => {
      if (item.name==='Peter') {return {...item, kor: 100}}
      return item;
    })
    setData(newData)
  }

  return (
    
    <>

      <div>{data[1].kor}</div>
      <Child getData={getData}/>   {/* key value 형태 */}
      <div>{greet}</div>

      <div>{data[1].name}</div>
      <div>{data[1].kor}</div>
      <button onClick={handleClick}>버튼</button>
      {tags}

      <table border ="1">
        <thead>
          <tr>
            <th>이름</th>
            <th>국어</th>
            <th>수학</th>
          </tr>
        </thead>
        <tbody>
          {data.map(item => {
            return (
              <tr>
                <td>{item.name}</td>
                <td>{item.kor}</td>
                <td>{item.math}</td>
              </tr>)
          })}
        </tbody>
      </table>

      <div>{extract()[0].name}</div>
      <div>{extract()[0].kor}</div>
      <div>{extract()[0].math}</div>

      {average()}
    </>
  )
}

export default App
