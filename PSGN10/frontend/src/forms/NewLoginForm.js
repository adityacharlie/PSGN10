import React, { useState } from 'react'
import './NewLoginForm.css'
import { Form, Input, Button, Checkbox } from 'antd';
import { UserOutlined, LockOutlined } from '@ant-design/icons';
import { getCookie, getTrans } from '../utils'
import axios from 'axios'
import { LOGIN, USER_TYPE} from '../api'
import { useHistory } from 'react-router-dom'
import store from "../Store";
import {LOGIN_USER} from "../actions/types";

export default function NewLoginForm(props){

  const history = useHistory()
  const [loginErrorMsg, setloginErrorMsg] = useState('')
  
  const onFinish = (values) => {

    return axios
            .post(LOGIN, values)
            .then(response => {
                const token = getCookie('csrftoken')
                axios.defaults.headers.common['X-CSRFToken'] = token

                axios.get(USER_TYPE).then(userTypeResponse => {
                    axios.get('/accounts/auth/user/').then(userResponse => {
                      const user = {
						...userResponse.data,
						...userTypeResponse.data,
                      }
                      store.dispatch({
						type: LOGIN_USER,
						payload: user,
					  })

                      history.push('/league')

                    })
                })

            })
            .catch(error => {

                setloginErrorMsg(getTrans('Could not login with provided username and password.'))
                
            })
    };

  return (
    <Form
      name="normal_login"
      className="login-form"
      initialValues={{
        username: '',
        password: '',
        remember: true,
      }}
      onFinish={onFinish}
    >
      <Form.Item
        name="username"
        rules={[
          {
            required: true,
            message: 'Please input your Username!',
          },
        ]}
      >
        <Input prefix={<UserOutlined className="site-form-item-icon" />} placeholder="Username" />
      </Form.Item>
      <Form.Item
        name="password"
        rules={[
          {
            required: true,
            message: 'Please input your Password!',
          },
        ]}
      >
        <Input
          prefix={<LockOutlined className="site-form-item-icon" />}
          type="password"
          placeholder="Password"
        />
      </Form.Item>
      <Form.Item>
        <Form.Item name="remember" valuePropName="checked" noStyle>
          <Checkbox>Remember me</Checkbox>
        </Form.Item>

        <a className="login-form-forgot" href="/">
          Forgot password
        </a>
      </Form.Item>
      <div className="input-feedback">{loginErrorMsg}</div>
      <Form.Item>
        <Button type="primary" htmlType="submit" className="login-form-button">
          Log in
        </Button>
        Or <a href="/">register now!</a>
      </Form.Item>
    </Form>
  )
}