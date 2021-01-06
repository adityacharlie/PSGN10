import React, { PureComponent } from 'react'
import axios from 'axios'
import { USER_TYPE } from './api'
import store from './Store'
import { LOGIN_USER } from './actions/types'
import { getCookie } from './utils'
import { Redirect } from 'react-router-dom'

class AppWrapper extends PureComponent {
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
                })
            })
        }
    }

    render() {
        const token = getCookie('csrftoken')
        if (!token) return <Redirect to={{ pathname: '/', state: { from: window.location.pathname } }} />

        return <div>{this.props.children}</div>
    }
}

export default AppWrapper
