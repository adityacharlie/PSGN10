import React, { useState } from 'react'
import { Calendar } from 'react-date-range'
import CalendarIcon from '../../assets/icons/calendar-icon.svg'
import { getShortDate } from '../../utils/dateHelpers'
import './DatePickerSingle.css'

export default function DatePickerSingle(props) {
    const [expanded, setExpanded] = useState(false)
    const [localDate, setLocalDate] = useState(Date.now())

    const handleDateChange = date => {
        setLocalDate(date)
        // props.handleFormUpdate('date', date)
        setExpanded(false)
    }

    return (
        <div className="datePicker__outerContainer height40">
            <div className="datePicker__innerContainer" onClick={() => setExpanded(!expanded)}>
                <div className="datePicker__leftBox">
                    <img src={CalendarIcon} alt="story title icon" />
                </div>
                <p className="addNew2__dateDisplay">{getShortDate(localDate)}</p>
            </div>

            {expanded && (
                <div className="datePicker__calendarContainer">
                    <Calendar onChange={handleDateChange} style={{ boxShadow: '2px 2px 8px 0px rgba(0,0,0,0.30)' }} />
                </div>
            )}
        </div>
    )
}
