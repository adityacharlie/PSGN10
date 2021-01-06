import React from 'react'
import { CustomInput, FormGroup } from 'reactstrap'
import PasswordInput from './PasswordInput'
import MyInput from './MyInput'

export default (field, formProps) => {
    switch (field.component) {
        case 'charField':
            return <MyInput key={field.name} {...field} {...formProps} />
        case 'password':
            return <PasswordInput key={field.name} {...field} {...formProps} />
        case 'checkbox':
            return (
                <FormGroup key={field.name} className="default-form--checkbox">
                    <CustomInput
                        id={field.name}
                        type={field.type}
                        label={field.label}
                        value={formProps.values[field.name]}
                        onChange={formProps.handleChange}
                    />
                </FormGroup>
            )
        default:
            return null
    }
}
