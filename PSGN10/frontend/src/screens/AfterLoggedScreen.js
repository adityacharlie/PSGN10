import React, { PureComponent } from 'react'
import { withRouter } from 'react-router-dom'
import { getCookie, getTrans } from '../utils'


class LoginScreen extends PureComponent {
	componentDidMount() {
		
	}

	render() {
        return (
            <span className="mr-3">{getTrans('Succesfully Logged')}</span>
        )
    }	
}



export default withRouter(LoginScreen)