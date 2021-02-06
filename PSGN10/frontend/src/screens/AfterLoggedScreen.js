import React, { PureComponent } from 'react'
import { withRouter } from 'react-router-dom'
import { getCookie, getTrans } from '../utils'
import BaseScreen from "./BaseScreen";


class LoginScreen extends PureComponent {
	componentDidMount() {
		
	}

	render() {
        return (
            <BaseScreen>
                <div>
                    <span className="mr-3">{getTrans('Succesfully Logged')}</span>
                </div>
            </BaseScreen>

        )
    }
}



export default withRouter(LoginScreen)