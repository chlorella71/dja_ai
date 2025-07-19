import React, { useCallback, useState, useEffect } from 'react'
import { Input, Button, Card, Space } from 'antd'
import { useDispatch, useSelector } from 'react-redux'
import { login } from '../../redux/authSlice'
import { useNavigate } from 'react-router-dom'

const initialState = {
  name: '',
  password: '',
}

const Login = () => {
  const [state, setState] = useState(initialState);
  const { name, password } = state;
  const dispatch = useDispatch();
  const navigator = useNavigate();
  const { status, user, error, isAuthenticated } = useSelector(state => state.auth);

  const handleLogin = useCallback(() => {
    dispatch(login(state));  // 비동기 액션 호출
  }, [dispatch, state]);

  // 로그인 성공 또는 실패 처리
  useEffect(() => {
    if (isAuthenticated) {
      navigator('/');
    } else if (status === 'failed') {
      alert(error);
    }
  }, [isAuthenticated, status, error, navigator]);

  const goToRegister = () => {
    navigator("/register");
  }

  return (
    <div style={{
      height: '100vh',
      display: "flex",
      alignItems: "center",
      justifyContent: 'center',
      background: "#f0f2f5"
    }}>
      <Card title="로그인" style={{ width: 400 }}>
        <Input
          placeholder='아이디'
          value={name}
          onChange={(e) => setState(prev => ({ ...prev, name: e.target.value }))}
          style={{ marginBottom: 16 }}
        />
        <Input.Password
          placeholder='비밀번호'
          value={password}
          onChange={(e) => setState(prev => ({ ...prev, password: e.target.value }))}
          style={{ marginBottom: 16 }}
        />
        <Space direction='vertical' style={{ width: '100%' }}>
          <Button type="primary" block onClick={handleLogin} loading={status === 'loading'}>
            로그인
          </Button>
          <Button type="link" block onClick={goToRegister}>
            아직 회원이 아니신가요? 회원가입
          </Button>
        </Space>
      </Card>
    </div>
  )
}

export default Login;
