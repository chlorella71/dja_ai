import EmployeeList from './employeeList';
import { Link } from 'react-router-dom';
import Register from './Register';
import Upgrade from './Upgrade';
import useEmployee from '../contexts/EmployeeContext';

const style ={
  display: "flex",
  flexDirection: "row",
  justifyContent: "space-between",
  alignItems: "center",
  gap: "10px",
  padding: "20px",
}

const Main = () => {
  const {mode, modes, handleClick} = useEmployee();
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

export default Main;