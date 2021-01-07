import React, { PureComponent } from 'react'
import { withRouter } from 'react-router-dom'
import { getCookie, getTrans } from '../utils'
import AuthWrapper from '../wrappers/AuthWrapper/AuthWrapper'
import LoginForm from '../forms/LoginForm'
import NewLoginForm from '../forms/NewLoginForm'

class LoginScreen extends PureComponent {
	componentDidMount() {
		const token = getCookie('csrftoken')

		if (token) {

		}
	}

	render() {
        return (
            <AuthWrapper title={getTrans('Login')}>
                <NewLoginForm />
            </AuthWrapper>
        )
    }	
}



export default withRouter(LoginScreen)