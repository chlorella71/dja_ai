import React, { useState, useCallback, useEffect } from 'react';
import { Input, Button, Card, Space, Form, message } from 'antd'; // Import Form and message
import { useDispatch, useSelector } from 'react-redux'; // Import useSelector
import { useNavigate } from 'react-router-dom';
import { register } from '../../redux/authSlice';

// 초기 폼 값 설정 (Form 컴포넌트 사용 시 이 initialState는 직접 사용되지 않을 수 있지만, 구조를 보여주기 위해 유지)
// Ant Design Form은 field prop을 통해 자체적으로 값을 관리합니다.
const initialFormValues = {
  name: '',
  password: '',
  confirm: '',
  age: null, // Ant Design Input의 value는 문자열이므로, 초기값을 빈 문자열로 설정하는 것이 일반적입니다.
  email: '',
  city: '',
};

const Register = () => {
  // Ant Design Form의 인스턴스를 생성합니다.
  const [form] = Form.useForm();
  const dispatch = useDispatch();
  const navigate = useNavigate();

  // Redux 상태에서 등록 관련 정보(로딩 상태, 에러, 사용자 정보)를 가져옵니다.
  const { status, user, error } = useSelector((state) => state.auth);

  // 등록 상태 변화에 따른 사이드 이펙트 처리
  useEffect(() => {
    if (status === 'succeeded' && user) {
      message.success('회원가입이 성공적으로 완료되었습니다!');
      // 회원가입 성공 후 로그인 페이지로 리다이렉션
      navigate('/login');
    } else if (status === 'failed' && error) {
      // 에러 메시지 표시
      message.error(`회원가입 실패: ${error}`);
    }
  }, [status, user, error, navigate]);

  // 폼 제출 핸들러 (Ant Design Form에서 자동으로 유효성 검사 후 호출됩니다)
  const onFinish = useCallback(
    (values) => {
      // 비밀번호와 비밀번호 확인 일치 여부 다시 한 번 확인 (Form validator가 일차적으로 처리)
      if (values.password !== values.confirm) {
        message.error('비밀번호와 비밀번호 확인이 일치하지 않습니다.');
        return;
      }
      const {confirm, ...userData}=values;
      // register thunk를 디스패치합니다.
      dispatch(register(userData));
      navigate('/login');
    },
    [dispatch]
  );

  // 폼 제출 실패 핸들러 (유효성 검사 실패 시 호출)
  const onFinishFailed = useCallback((errorInfo) => {
    console.log('회원가입 실패 (유효성 검사):', errorInfo);
    message.error('입력 양식을 올바르게 작성해주세요.');
  }, []);

  return (
    <div
      style={{
        height: '100vh',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        background: '#f0f2f5',
      }}
    >
      <Card title="회원가입" style={{ width: 400 }}>
        {/* Ant Design Form 컴포넌트로 전체 폼을 감쌉니다. */}
        <Form
          form={form} // form 인스턴스를 연결
          name="register"
          initialValues={initialFormValues} // 초기 값 설정
          onFinish={onFinish} // 제출 시 호출될 함수
          onFinishFailed={onFinishFailed} // 유효성 검사 실패 시 호출될 함수
          autoComplete="off" // 자동 완성 기능 비활성화
        >
          <Form.Item
            name="name" // 필드 이름을 지정 (state의 키와 일치)
            rules={[
              { required: true, message: '아이디를 입력해주세요!' },
              { min: 4, message: '아이디는 최소 4자 이상이어야 합니다.' },
            ]}
          >
            <Input placeholder="아이디" />
          </Form.Item>

          <Form.Item
            name="password"
            rules={[
              { required: true, message: '비밀번호를 입력해주세요!' },
              { min: 6, message: '비밀번호는 최소 6자 이상이어야 합니다.' },
            ]}
            hasFeedback // 비밀번호 강도 등에 대한 시각적 피드백 제공
          >
            <Input.Password placeholder="비밀번호" />
          </Form.Item>

          <Form.Item
            name="confirm"
            dependencies={['password']} // password 필드에 의존
            hasFeedback
            rules={[
              { required: true, message: '비밀번호 확인을 입력해주세요!' },
              ({ getFieldValue }) => ({
                validator(_, value) {
                  if (!value || getFieldValue('password') === value) {
                    return Promise.resolve();
                  }
                  return Promise.reject(new Error('비밀번호가 일치하지 않습니다!'));
                },
              }),
            ]}
          >
            <Input.Password placeholder="비밀번호 확인" />
          </Form.Item>

          <Form.Item
            name="age"
            rules={[
              { required: true, message: '나이를 입력해주세요!' },
              { type: 'number', min: 1, max: 120, transform: value => Number(value) || undefined, message: '유효한 나이를 입력해주세요.' },
            ]}
          >
            <Input type="number" placeholder="나이" />
          </Form.Item>

          <Form.Item
            name="email"
            rules={[
              { required: true, message: '이메일을 입력해주세요!' },
              { type: 'email', message: '유효한 이메일 주소를 입력해주세요.' },
            ]}
          >
            <Input placeholder="이메일" />
          </Form.Item>

          <Form.Item name="city" rules={[{ required: true, message: '도시를 입력해주세요!' }]}>
            <Input placeholder="도시" />
          </Form.Item>

          <Form.Item>
            <Space direction="vertical" style={{ width: '100%' }}>
              <Button type="primary" htmlType="submit" block loading={status === 'loading'}>
                회원가입
              </Button>
              <Button type="link" block onClick={() => navigate('/login')}>
                이미 회원이신가요? 로그인
              </Button>
            </Space>
          </Form.Item>
        </Form>
      </Card>
    </div>
  );
};

export default Register;