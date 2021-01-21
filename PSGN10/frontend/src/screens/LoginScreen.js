import React, { PureComponent } from 'react'
import { withRouter } from 'react-router-dom'
import { getCookie, getTrans } from '../utils'
import AuthWrapper from '../wrappers/AuthWrapper/AuthWrapper'
import LoginForm from '../forms/LoginForm'
import NewLoginForm from '../forms/NewLoginForm'
import { redirectUser } from '../utils/handleRedirects'
import { USER_TYPE } from '../api'
import { LOGIN_USER } from '../actions/types'
import store from '../Store'
import axios from 'axios'

class LoginScreen extends PureComponent {
	componentDidMount() {
		const token = getCookie('csrftoken')

		if (token) {
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

					redirectUser(user, this.props.history)
				})

			})

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