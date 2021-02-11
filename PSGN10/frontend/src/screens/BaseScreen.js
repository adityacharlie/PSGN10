import { PureComponent } from 'react'
import Navbar from '../components/Navbar/Navbar'



class BaseScreen extends PureComponent {
    render() {
        return (
            <div>
                <Navbar />
            </div>
        )
    }
}

export default BaseScreen