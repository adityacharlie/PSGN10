import { createStore, applyMiddleware } from 'redux'
import { composeWithDevTools } from 'redux-devtools-extension'
import { createLogger } from 'redux-logger'
import rootReducer from './reducers'
import reduxThunk from 'redux-thunk'

let middleware = [reduxThunk]
if (process.env.NODE_ENV === 'development') {
    middleware = [...middleware, createLogger()]
}

const store = createStore(rootReducer, composeWithDevTools(applyMiddleware(...middleware)))

export default store