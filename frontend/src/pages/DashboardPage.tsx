import React from 'react'
import '../DashboardPage.css';
import Navbar from '../components/Navbar';
import SwitchWQ from '../components/SwitchWQ';
import SwitchPC from '../components/SwitchCP';
import SwitchYesNo from '../components/SwitchYesNo';
import SliderFG from '../components/SliderFG';

const DashboardPage = () => {
  return (
    <>
        <div className="flex flex-col min-w-[800px] bg-custombg">
            <Navbar />
            <div className="container">
                <div className="container-center">
                    
                    <div className="heading-text">
                      Sara's Dashboard 
                      
                      <div className="sub-heading-text ">
                        Customize your Greeting
                      </div > 

                      <SwitchWQ/>
                      <SwitchPC/>
                      <SwitchYesNo/>  
                      <SliderFG/>                
                    </div>
                    
                    

                    {/*<div className="sub-heading-text ">
                      Notification
                    </div >

                    <div className="sub-sub-heading-text ">
                      Get your report emailed to you
                    </div >

                    <div className="sub-sub-heading-text ">
                      Set a time to receive your report
                    </div >*/}

                    
                    
                </div>
            </div>
        </div>
    </>  
    
  )
}

export default DashboardPage