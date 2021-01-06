import axios from 'axios'
import { LOGOUT } from '../api'
import { delete_cookie } from '../utils'

export const logoutUser = () => {
    return dispatch => {
        return axios.get(LOGOUT).then(response => {
            console.log('logout response', response)
            delete axios.defaults.headers.common['X-CSRFToken']
            delete_cookie('csrftoken')
            setTimeout(() => {
                window.location.href = '/'
            }, 500)
        })
    }
}
