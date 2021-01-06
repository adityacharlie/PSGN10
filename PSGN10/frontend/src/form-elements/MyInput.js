import React, { PureComponent } from 'react'
import { FormGroup, Input, Label } from 'reactstrap'
import classnames from 'classnames'
import { ErrorMessage } from 'formik'

class MyInput extends PureComponent {
    render() {
        const {
            name,
            label,
            placeholder,
            type,
            values,
            handleChange,
            handleBlur,
            errors,
            touched,
        } = this.props

        return (
            <FormGroup key={name}>
                <Label htmlFor={name}>{label}</Label>
                <Input
                    id={name}
                    placeholder={placeholder}
                    type={type}
                    value={values[name]}
                    onChange={handleChange}
                    onBlur={handleBlur}
                    className={classnames({
                        error: errors[name] && touched[name],
                    })}
                />
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

export default MyInput
