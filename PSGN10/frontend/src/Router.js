import LoginScreen from './screens/LoginScreen'
import LogoutScreen from './screens/LogoutScreen'
import LeagueScreen from './screens/LeagueScreen'
import AfterLoggedScreen from './screens/AfterLoggedScreen'
import { connect } from 'react-redux'
import { BrowserRouter as Router, Route } from 'react-router-dom'

const AppRouter = props => {
    return (
        <Router>
        	<div>
        		<Route path="/" exact component={LoginScreen} />
                <Route path="/logout" exact component={LogoutScreen} />
                <Route path="/afterlogged" exact component={AfterLoggedScreen} />
                <Route path="/league" exact component={LeagueScreen} />
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