import React, { PureComponent } from 'react'
import logo from '../../assets/images/logo.svg'
import logoWhite from '../../assets/images/logo.png'
import { Link } from 'react-router-dom'

class Logo extends PureComponent {
    render() {
        const { white } = this.props

        return (
            <Link to="/">
                <img src={white ? logoWhite : logo} alt="logo" />
            </Link>
        )
    }
}

export default Logo
