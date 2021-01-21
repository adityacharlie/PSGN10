import React, { PureComponent } from 'react'
import { connect } from 'react-redux'
import { logoutUser } from '../actions/AuthActions'
import { Button } from 'reactstrap'
import { getTrans } from '../utils'

class LogoutScreen extends PureComponent {

	componentDidMount() {

	}

	render() {
		const { isLoggedIn, logoutUser } = this.props

        return (
        	<div className="d-none d-lg-flex d-xl-flex">
	            <Button
	                onClick={logoutUser}
	                color="primary-dark"
	                className="btn d-inline-flex align-items-center"
	            >
	                <strong>{getTrans('Log out')}</strong>
	            </Button>
	        </div>
        )
    }	
}

const mapStateToProps = state => {
    return {
        user: state.auth.user,
        isLoggedIn: state.auth.isLoggedIn,
    }
}

export default connect(
    mapStateToProps,
    { logoutUser }
)(LogoutScreen)