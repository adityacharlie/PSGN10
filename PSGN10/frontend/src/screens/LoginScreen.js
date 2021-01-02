import React, { PureComponent } from 'react'
import { withRouter } from 'react-router-dom'
import { getCookie, getTrans } from '../utils'

class LoginScreen extends PureComponent {
	componentDidMount() {
		const token = getCookie('csrftoken')

		if (token) {

		}
	}	
}



export default withRouter(LoginScreen)