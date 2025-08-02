import './App.css'
import Main from './components/Main'
import {Routes, Route} from "react-router-dom"
import { EmployeeProvider } from './contexts/EmployeeContext';

function App() {

  return (
    <>
      <EmployeeProvider>
        <Routes>
          <Route path="/" element={<Main />}/>
        </Routes>
      </EmployeeProvider>
    </>
  )
}

export default App;
