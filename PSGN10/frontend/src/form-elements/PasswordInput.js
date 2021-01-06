import React, { PureComponent } from 'react'
import { FormGroup, Input, Label } from 'reactstrap'
import classnames from 'classnames'
import { IoMdEye, IoMdEyeOff } from 'react-icons/io'
import { ErrorMessage } from 'formik'
import styled from 'styled-components'

class PasswordInput extends PureComponent {
    state = {
        passwordHidden: true,
    }

    togglePasswordShow = e => {
        e.preventDefault()
        this.setState({
            passwordHidden: !this.state.passwordHidden,
        })
    }

    render() {
        const {
            name,
            label,
            placeholder,
            handleBlur,
            errors,
            touched,
            values,
            handleChange,
        } = this.props

        return (
            <FormGroup key={name}>
                <Label htmlFor={name}>{label}</Label>
                <Input
                    id={name}
                    placeholder={placeholder}
                    type={this.state.passwordHidden ? 'password' : 'text'}
                    value={values[name]}
                    onChange={handleChange}
                    onBlur={handleBlur}
                    className={classnames('password-input', {
                        error: errors[name] && touched[name],
                    })}
                />
                <PasswordButton
                    onClick={this.togglePasswordShow}
                    className="btn btn-link"
                    type="button"
                >
                    {this.state.passwordHidden ? <IoMdEye /> : <IoMdEyeOff />}
                </PasswordButton>
                <ErrorMessage
                    component={() => (
                        <div className="input-feedback">{errors[name]}</div>
                    )}
                    name={name}
                />
            </FormGroup>
        )
    }
}

export default PasswordInput

const PasswordButton = styled.button`
    font-size: 20px;
    color: #777;
    cursor: pointer;
    position: absolute;
    right: 7px;
    top: 24px;
    &.btn-link {
        color: #777;
    }
`
