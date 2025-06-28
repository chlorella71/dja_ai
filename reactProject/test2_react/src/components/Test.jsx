import React from 'react'
import { useDispatch, useSelector } from 'react-redux'

const Test = () => {
    const {color} = useSelector(state=>state.color) // store에 등록된 color를 바로 받음
  return (
    <>
        <div>{color}</div>
    </>
  )
}

export default Test
