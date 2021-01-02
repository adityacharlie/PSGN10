import LoginScreen from './screens/LoginScreen'
import { connect } from 'react-redux'
import { BrowserRouter as Router, Route } from 'react-router-dom'

const AppRouter = props => {
    return (
        <Router>
        	<div>
        		<Route path="/" exact component={LoginScreen} />
        	</div>
        </Router>
    )
}

const mapStateToProps = state => {
	return {
		isLoggedIn: state.auth.isLoggedIn,
	}
}

export default connect(mapStateToProps)(AppRouter)