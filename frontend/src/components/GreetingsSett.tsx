import axios from 'axios';
import '../DashboardPage.css';
import SwitchWQ from './SwitchWQ'

// Component which displays the welcome message on the today page. It includes a greeting, the date and word of the day
const GreetingsSett = () => {
    return (
        <>
            <div className="sub-heading-text">
            Customize your Greeting
            <SwitchWQ/>
            </div>
        </>
    )
}

export default GreetingsSett