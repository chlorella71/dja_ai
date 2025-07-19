import React from 'react';
import {Button, Space} from 'antd';
import { useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { logout } from '../redux/authSlice';

const style = {
    display: "flex",
    alignItems: "center",
    justifyContent:" space-between",
    padding: "0 24px",
    height: "100%", 
    backgroundColor: "#2c3e50",
    boxShadow: "0 2px 8px #f0f1f2",
}

const HeaderBar = () => {
  const navigate = useNavigate()
  const dispatch = useDispatch();
  const { user } = useSelector(state => state.auth);
  const handleLogout =()=>{
    dispatch(logout());
    navigate('/login')
  }
  return (
    <div style={style}>
        <div style={{fontSize: "20px", fontWeight: "bold", color: "#1890ff"}}>
          MyLogo
        </div>
        <Space>
          {user ? (
              <>
                <span style={{color: 'white'}}>{user.name}님</span>
                <Button type="primary" danger onClick={handleLogout}>로그아웃</Button>
              </>
          ):(
            <>
              <Button onClick={()=>navigate("/login")}>
                  로그인
              </Button>
              <Button onClick={()=>navigate("/register")}>
                회원가입
              </Button>
            </>
           
          )}
            
        </Space>
    </div>
  )
}

export default HeaderBar