import * as actionTypes from '../actions/types'

const INITIAL_STATE = {
    user: {},
    isLoggedIn: false,
}

export default (state = INITIAL_STATE, action) => {
    const { type, payload } = action

    switch (type) {
        case actionTypes.LOGIN_USER:
            return {
                ...state,
                user: payload,
                isLoggedIn: true,
            }
        case actionTypes.LOGOUT_USER:
            return INITIAL_STATE
        default:
            return state
    }
}