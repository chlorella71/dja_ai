import React, { useState } from 'react'

// {data: data}

const Child = ({getData}) => {

    // const {data} = props;

    // const handleClick = () => {
    //     setData(data.map(item => {
    //         if (item.name === 'Peter') {
    //             return {...item, kor: 1000}}
    //         return item
    //     }))
    // }

    const[info, setInfo] = useState("Child: 안녕하세요!!")

    const handleClick = () => {

        getData(info);

        // setData(prev => prev.map(item => {
        //     if (item.name === 'Peter') {
        //         return {...item, kor: 1000}}
        //     return item
        // }))
    }

  return (
    <>
      <div>Hello World!!!</div>
      <button onClick={handleClick}>버튼</button>

      <div>...Child</div>
      <br />
    </>
  )
}

export default Child
