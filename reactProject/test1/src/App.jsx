import { useState } from 'react'
import './App.css'
import Child from './components/Child'
import Form, { a } from './components/Form'
import Info from './components/Info'
import Fetch from './components/Fetch'

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

const initialInfoData = { name: "John", age: 30, job: "frontend"}

const App = () => {

  const [infoData, setInfoData] = useState(initialInfoData)

  const getFormData = (param) => {
    console.log("자식의 데이터:", param);
  }

  const [b, setB] = useState(a)

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

      <Fetch />

      <div>...Fetch</div><br /><br />

      <div>이름: {infoData.name}</div>
      <div>나이: {infoData.age}</div>
      <div>직업: {infoData.job}</div>      
      
      <Info infoData={infoData} setInfoData={setInfoData}></Info>

      <div>...Info</div><br /><br />

      <div>Form의 변수 a의 값이 App의 state b에 담겨저서 출력됨:{b}</div><br />

      <Form 함수={getFormData} />

      <div>...Form</div><br /><br />

      <div>데이터정보</div>
      <div>{data.id}</div>
      <div>{data.pw}</div>

      <br />

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
