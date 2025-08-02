import React, { useEffect, useState } from 'react';
import { connect } from 'react-redux';
import { handleUpgrade } from '../redux/employeeSlice';

const formStyle = {
  display: 'flex',
  flexDirection: 'column',
  width: '300px',
  margin: '20px auto',
  padding: '20px',
  border: '1px solid #ccc',
  borderRadius: '10px',
  backgroundColor: '#f9f9f9',
  boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)'
};

const labelStyle = {
  marginBottom: '10px',
  display: 'flex',
  flexDirection: 'column',
  fontWeight: 'bold',
  color: '#333'
};

const inputStyle = {
  padding: '8px',
  borderRadius: '5px',
  border: '1px solid #ccc',
  fontSize: '14px'
};

const Upgrade = ({name, upInfo, handleUpgrade}) => {
    const [info, setInfo] = useState(upInfo ? upInfo:{});

    const handleChange = (e) =>{
        setInfo(prev=>({...prev, [e.target.name]: e.target.value}))
    }

    const handleSubmit=(e)=>{
        e.preventDefault();
        handleUpgrade(info)
    }

    useEffect(()=>{
      console.log("name", name)
      setInfo({name, ...upInfo})
    }, [name])

  return (
    <form style={formStyle} onSubmit={handleSubmit}>
      <label style={labelStyle}>
        Name
        <input 
          type="text" 
          name="name" 
          style={inputStyle} 
          value={name && info.name} 
          disabled
        />
      </label>
      <label style={labelStyle}>
        Age
        <input type="number" name="age" style={inputStyle} value={name && info.age} onChange={handleChange}/>
      </label>
      <label style={labelStyle}>
        Job
        <input type="text" name="job" style={inputStyle} value={name && info.job} onChange={handleChange}/>
      </label>
      <label style={labelStyle}>
        Language
        <input type="text" name="language" style={inputStyle} value={name && info.language} onChange={handleChange}/>
      </label>
      <label style={labelStyle}>
        Pay
        <input type="number" name="pay" style={inputStyle} value={name && info.pay} onChange={handleChange}/>
      </label>
      <button>수정</button>
    </form>
  );
};

export default connect(
  ({employee})=>({
    name: employee.name,
    upInfo: employee.upInfo
  }),
  {handleUpgrade}
)(Upgrade);
