import axios from 'axios'

export const redirectUser = (user, history) => {
    console.log(user,history);
    switch (user.user_type) {
        case 'analyst':
            axios.get(`/accounts/analyst/${user.id}/groups/`).then(response => {
                const firstCompanyGroup = response.data.results[0] || {}
                history.push(`/app/news-feed/${firstCompanyGroup.id}`)
            })
            break

        case 'customer':
                history.push('/afterlogged')
            break

        default:
            return history.push('/app/settings-details')
    }
}
