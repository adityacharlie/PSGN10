import { getTrans } from './index'

export const validateForm = (values, fields) => {
    let errors = {}
    Object.entries(values).forEach(([key, value]) => {
        const field = fields.find(field => field.name === key)
        if (!value && field.required) {
            errors[key] = getTrans('Required')
        }
    })

    if (!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(values.email) && values.email) {
        errors.email = getTrans('Invalid email address')
    }

    if (values.password !== values.password2 && values.password2) {
        errors.password2 = getTrans("Passwords don't match.")
    }

    console.log('errors', errors)

    return errors
}
