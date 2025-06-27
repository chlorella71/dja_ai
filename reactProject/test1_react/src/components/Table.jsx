import React, { useState,useEffect } from 'react'
import Tr from './Tr'

const data = [
    { name: "john", age: 21, email: "jjj@example.com", city: "NewYork" },
    { name: "sue", age: 30, email: "sue1212@example.com", city: "London" },
    { name: "mike", age: 29, email: "mkkkk9@example.com", city: "Seoul" },
]

const Table = ({obj}) => {
    const [ infos, setInfos ] = useState(data)
    useEffect(()=>{
        const execute = () => {
            obj && setInfos(prev=>[...prev, obj])
        }
        execute()
    },[obj])
    
    
  return (
    <>
        <table style={{border: '1px solid black',}} border={'1'}>
            <thead>
                <tr>
                    {Object.keys(infos[0]).map(item => (<th key={item}>{item}</th>))}
                </tr>             
            </thead>
            <tbody>
                {infos.map(infos => (<Tr key={infos.name} infos={infos}/>))}
            </tbody>
        </table>
 
    </>
  )
}

export default Table
