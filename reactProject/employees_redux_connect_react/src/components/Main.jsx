import React, { useCallback} from 'react'
import EmployeeList from './EmployeeList';
import { Link } from 'react-router-dom';
import Register from './Register';
import Upgrade from './Upgrade';
import { connect } from 'react-redux';
import { 
  changeMode, 
  resetState, 
  handleDelete, 
} from '../redux/employeeSlice';



const style ={
  display: "flex",
  flexDirection: "row",
  justifyContent: "space-between",
  alignItems: "center",
  gap: "10px",
  padding: "20px",
}

const modes = [ "register", "upgrade", "delete", "초기화"]
const Main = ({mode, name, handleDelete, resetState, changeMode}) => {
    const handleClick = useCallback((mod) =>{
        if(mod === 'delete'){
          if(name){
            handleDelete()
          }else{
            alert("직원을 선택해 주세요.")
          }
        }else if(mod==='초기화'){
          resetState();
        }else if(mod==='upgrade'){
          if(name){
            changeMode(mod)
          }else{
            alert("직원을 선택해 주세요.")
          }
        }else{
          changeMode(mod)
        }
        // setName(null)
    }, [name])
  
  return (
    <>
      <div>
          <EmployeeList/>
      </div>
      <div style={style}>
          {modes.map(mod=><Link 
                              to="/"
                              onClick={(e)=>{
                                e.preventDefault();
                                handleClick(mod)
                              }}
                            >
                              {mod}
                            </Link>
                    )
          }
      </div>
       <div>
        {mode === "register" && (
          <Register/>
        )}
        {mode === "upgrade" && (
          <Upgrade/>
        )}
      </div>
    </>
  )
}

export default connect(
  ({employee}) => ({
    mode: employee.mode,
    name: employee.name,
  }),
  {
    resetState,handleDelete, changeMode
  }
)(Main);