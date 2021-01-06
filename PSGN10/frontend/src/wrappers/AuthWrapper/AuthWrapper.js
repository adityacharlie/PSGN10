import React, { PureComponent } from 'react'
import styled from 'styled-components'
import { Link } from 'react-router-dom'
import { getCookie, getTrans } from '../../utils'
import Logo from '../../components/Logo/Logo'
import axios from 'axios'

class AuthWrapper extends PureComponent {
    componentDidMount() {
        const token = getCookie('csrftoken')

        if (token) {
            axios.defaults.headers.common['X-CSRFToken'] = token
        }
    }

    render() {
        const { title } = this.props

        return (
            <Wrapper>
                <AuthBody>
                    <div className="text-center mb-3">
                        <Logo white />
                    </div>
                    <Inner>
                        <Title>{title}</Title>
                        {this.props.children}
                    </Inner>
                    <Footer>
                        <span className="mr-3">{getTrans('© 2018 Kaitongo Inc.')}</span>
                        <Link to="/terms" className="mr-3">
                            {getTrans('Terms')}
                        </Link>
                        <Link to="/privacy" className="mr-3">
                            {getTrans('Privacy')}
                        </Link>
                        <Link to="/forgot-password" className="">
                            {getTrans('Forgot password?')}
                        </Link>
                    </Footer>
                </AuthBody>
            </Wrapper>
        )
    }
}

export default AuthWrapper

const Wrapper = styled.div`
    height: 100vh;
    background: #05183d;
    padding: 6rem 0;
`

const AuthBody = styled.div`
    max-width: 388px;
    margin: auto;
`

const Inner = styled.div`
    background: #fff;
    padding: 25px;
    border-radius: 8px;
    box-shadow: 0 1px 4px 0 rgba(0, 0, 0, 0.2);
    margin-bottom: 1rem;
`

const Title = styled.h2`
    margin-bottom: 1.5rem;
    text-align: left;
`

const Footer = styled.div`
    text-align: left;
    a,
    span {
        font-size: 12px;
        font-weight: 600;
        text-align: left;
        color: rgba(255, 255, 255, 0.4);
    }
`
