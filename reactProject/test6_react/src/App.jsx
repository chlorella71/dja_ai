import { useEffect, useMemo, useState } from 'react'
import './App.css'
import ProductDisplay from './components/ProductDisplay'
import UserInfo from './components/UserInfo'
import MyComponent from './components/MyComponent'
import FocusInput from './components/FocusInput'
import Timer from './components/Timer'
import ValueTracker from './components/ValueTracker'

const initialStateUser = {
  name:'정희준',
  age:30,
  count:100,
}

function App() {
  const [text, setText] = useState()
  const [user, setUser] = useState(initialStateUser)
  const [toggle, setToggle] = useState(false)
  const [myValue, setMyValue] = useState(0)
  const items = useMemo(() => [
    {id: 1, name: '사과'},
    {id: 2, name: '바나나'},
    {id: 3, name: '딸기'}
  ], [])
  const memorizedUser = useMemo(()=> {
    return {name: user.name, age:user.age}
  }, [user])
  useEffect(()=>{
    console.log('count: ', user.count)
  },[user])
  return (
    <>
      <div>
        <h2>ProductDisplay</h2>
        <input type='text' value={text} onChange={(e) => setText(e.target.value)} />
        <ProductDisplay products={items} filterText={text} />
      </div>
      <div>
        <UserInfo user={memorizedUser} />
        <input type='text' value={user.name} onChange={(e)=>setUser(prev=>({...prev, name:e.target.value}))} />
        <input type='number' value={user.age} onChange={e=>setUser(prev=>({...prev, age:e.target.value}))} />
        <button onClick={()=>setUser(prev=>({...prev, count:prev.count + 1}))}>count</button>
      </div>
      <div>
        <h2>StaticOptions</h2>
        <button onClick={()=>setToggle(prev=>!prev)}>toggle</button>
        {toggle && <MyComponent />}
      </div>
      <div>
        <FocusInput />
      </div>
      <div>
        <h2>Timer</h2>
        <Timer />
      </div>
      <div>
        <h2>ValueTracker</h2>
        <button onClick={()=>setMyValue(myValue+1)}>increase value</button>
        <ValueTracker value={myValue} />
      </div>
    </>
  )
}

export default App
