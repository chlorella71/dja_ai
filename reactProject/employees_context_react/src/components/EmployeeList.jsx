import React, { useEffect, useState }  from 'react';
import { Link } from 'react-router-dom';
import InfoTable from './InfoTable';
import useEmployee from '../contexts/EmployeeContext';

const style ={
  display: "flex",
  flexDirection: "row",
  justifyContent: "space-between",
  alignItems: "center",
  gap: "10px",
  padding: "20px",
}

const initialState = {
  name: null, 
  age: null, 
  job: null, 
  language: null, 
  pay: null
}


const EmployeeList = () => {
  const {name, infos, handleSearchName} = useEmployee()
  const [info, setInfo] = useState(initialState)

  const handleClick = (n) =>{
     setInfo(infos?.filter(info=>info.name===n)[0])
     handleSearchName(n)
  }

  useEffect(()=>{
    console.log("info", name)
    setInfo(infos?.filter(info=>info.name===name)[0])
  }, [name, infos])

  return (
    <>
      <div style={style}>
          {infos.map(info=><Link 
                              to="/" 
                              key={info.name}
                              onClick={()=>handleClick(info.name)}
                            >
                              {info.name}
                            </Link>)}
      </div>
      {name ? <InfoTable info={info}/> : <InfoTable info={initialState}/>}
    </>
    
  )
}
export default EmployeeList