import { Button, Card, Input, InputNumber, Space } from 'antd';
import React, { useCallback, useEffect, useState } from 'react';
import {useDispatch, useSelector} from 'react-redux'
import { register } from '../../redux/authSlice';
import {useNavigate} from 'react-router-dom'


// status: "idle",
// user: '',
// error: null,
// isAuthenticated: false

const initialState = {
  name: null,
  password: null,
  confirm: null,
  age: null,
  email: null,
  city: null
}

const Register = () => {
    const [state, setState] = useState(initialState);
    const {name, password, confirm, age, email, city} = state
    const dispatch = useDispatch()
    const navigate = useNavigate()

    const handleChange = useCallback((e) => {
      setState(prev=>({
        ...prev, [e.target.name]:e.target.value
      }))
    } ,[setState])

    const handleRegister = useCallback(async() => {
      try {
        if (password !== confirm) {
          alert('비밀번호가 일치하지 않습니다.')
          return
        }
        const {confirm: _, ...userData} =state
        await dispatch(register(userData)).unwrap()
        navigate('/')
      } catch (err) {
        alert('회원가입 실패: '+ err)
      }
      
    }, [dispatch, state, navigate])

  return (
    <div style={{
        height: '100vh', 
        display: "flex", 
        alignItems: "center",
        justifyContent: 'center',
        background: "#f0f2f5"
    }}>
        <Card title="회원가입" style={{width: 400}}>
            <Input
                name="name"
                placeholder='아이디'
                value={name}
                onChange={handleChange}
                style={{marginBottom: 16}}
            />
            <Input.Password
                name="password"
                placeholder='비밀번호'
                value={password}
                onChange={handleChange}
                style={{marginBottom: 16}}
            />
            <Input.Password
                name="confirm"
                placeholder='비밀번호 확인'
                value={confirm}
                onChange={handleChange}
                style={{marginBottom: 16}}
            />
            <InputNumber
                placeholder='나이'
                value={age}
                onChange={(value) => 
                  setState((prev) => ({...prev, age: value}))
                }
                style={{marginBottom: 16}}
            />
            <Input
                name="email"
                type="email"
                placeholder='이메일'
                value={email}
                onChange={handleChange}
                style={{marginBottom: 16}}
            />
            <Input
                name="city"
                placeholder='도시'
                value={city}
                onChange={handleChange}
                style={{marginBottom: 16}}
            />
            <Space direction='vertical' style={{width: '100%'}}>
                <Button type="primary" block onClick={handleRegister}>
                    회원가입
                </Button>
                <Button type="link" block onClick={()=>navigate('/login')}>
                    이미 회원이신가요? 로그인
                </Button>
            </Space>
        </Card>
      
    </div>
  );
}

export default Register;
