export const getMonth3Char = monthNum => {
    if (monthNum === 0) {
        return 'Jan'
    } else if (monthNum === 1) {
        return 'Feb'
    } else if (monthNum === 2) {
        return 'Mar'
    } else if (monthNum === 3) {
        return 'Apr'
    } else if (monthNum === 4) {
        return 'May'
    } else if (monthNum === 5) {
        return 'Jun'
    } else if (monthNum === 6) {
        return 'Jul'
    } else if (monthNum === 7) {
        return 'Aug'
    } else if (monthNum === 8) {
        return 'Sep'
    } else if (monthNum === 9) {
        return 'Oct'
    } else if (monthNum === 10) {
        return 'Nov'
    } else if (monthNum === 11) {
        return 'Dec'
    } else if (monthNum === 12) {
        return 'Jan'
    } else if (monthNum === 13) {
        return 'Feb'
    }
}

const getMonthFull = monthNum => {
    if (monthNum === 0) {
        return 'January'
    } else if (monthNum === 1) {
        return 'February'
    } else if (monthNum === 2) {
        return 'March'
    } else if (monthNum === 3) {
        return 'April'
    } else if (monthNum === 4) {
        return 'May'
    } else if (monthNum === 5) {
        return 'June'
    } else if (monthNum === 6) {
        return 'July'
    } else if (monthNum === 7) {
        return 'August'
    } else if (monthNum === 8) {
        return 'September'
    } else if (monthNum === 9) {
        return 'October'
    } else if (monthNum === 10) {
        return 'November'
    } else if (monthNum === 11) {
        return 'December'
    }
}

export const getDay3Char = day => {
    if (day === 0) {
        return 'Sun'
    } else if (day === 1) {
        return 'Mon'
    } else if (day === 2) {
        return 'Tue'
    } else if (day === 3) {
        return 'Wed'
    } else if (day === 4) {
        return 'Thu'
    } else if (day === 5) {
        return 'Fri'
    } else if (day === 6) {
        return 'Sat'
    }
}

export const getFullFormattedDate = dateInput => {
    const dateObj = new Date(dateInput)
    const fullMonth = getMonthFull(dateObj.getMonth())
    const fullDate = dateObj.getDate()
    const fullYear = dateObj.getFullYear()

    return fullMonth + ' ' + fullDate + '/' + fullYear
}

export const getShortDate = dateInput => {
    const dateObj = new Date(dateInput)
    const shortMonth = getMonth3Char(dateObj.getMonth())
    const fullDate = dateObj.getDate()
    const fullYear = dateObj.getFullYear()

    return shortMonth + ' ' + fullDate + '/' + fullYear.toString().substr(-2)
}