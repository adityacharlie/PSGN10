import React, { PureComponent } from 'react'
import './LoginForm.css'
import { validateForm } from '../utils/validateForm'
import { Button } from 'reactstrap'
import { Form, Formik } from 'formik'
import RenderField from '../form-elements/RenderField'
import { getCookie, getTrans } from '../utils'
import axios from 'axios'
import { LOGIN } from '../api'
import { LOGIN_USER } from '../actions/types'
import store from '../Store'
import { withRouter } from 'react-router-dom'
// import { redirectUser } from '../utils/handleRedirects'
// import dotProp from 'dot-prop-immutable'

const fields = [
    {
        label: 'Username',
        value: '',
        name: 'username',
        component: 'charField',
        placeholder: 'Enter your Username',
        type: 'text',
        required: true,
    },
    {
        label: 'Password',
        value: '',
        name: 'password',
        component: 'password',
        placeholder: 'Password',
        type: 'password',
        required: true,
    },
    {
        label: 'Remember me',
        value: false,
        name: 'remember_me',
        component: 'checkbox',
        type: 'checkbox',
        required: false,
    },
]

class LoginForm extends PureComponent {
    state = {
        loginErrorMsg: '',
    }

    onSubmit = (values, { setSubmitting }) => {
        const { history, location } = this.props

        setSubmitting(false)

        return axios
            .post(LOGIN, values)
            .then(response => {
                const token = getCookie('csrftoken')
                axios.defaults.headers.common['X-CSRFToken'] = token

                history.push(`/afterlogged`)
                
            })
            .catch(error => {
                console.log('login error', error.response)
                this.setState({
                    loginErrorMsg: getTrans('Could not login with provided username and password.'),
                })
            })
    }

    render() {
        return (
            <Formik
                initialValues={{
                    username: '',
                    password: '',
                    remember_me: false,
                }}
                validate={values => validateForm(values, fields)}
                onSubmit={this.onSubmit}
                render={({ status, isSubmitting, ...formProps }) => (
                    <Form className="login-form">
                        {fields.map(field => {
                            return RenderField(field, formProps)
                        })}
                        <div className="input-feedback">{this.state.loginErrorMsg}</div>
                        <div className="text-right">
                            <Button color="primary" type="submit" disabled={isSubmitting}>
                                {getTrans('Login')}
                            </Button>
                        </div>
                    </Form>
                )}
            />
        )
    }
}

export default withRouter(LoginForm)
