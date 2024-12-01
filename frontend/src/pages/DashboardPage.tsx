import React from 'react'
import '../DashboardPage.css';
import Navbar from '../components/Navbar';
import SwitchWQ from '../components/SwitchWQ';
import SwitchPC from '../components/SwitchCP';
import SwitchYesNo from '../components/SwitchYesNo';
import SliderFG from '../components/SliderFG';
import TimeBubble from '../components/TimeBubble';
import AutoCompleteCE from '../components/AutocompleteCE'

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
                      <div className="flex justify-start pb-3">
                      <div className="circle bg-[#D50000]"></div>
                      <div className="circle bg-[#E67C73]"></div>
                      <div className="circle bg-[#F4511E]"></div>
                      <div className="circle bg-[#F6BF26]"></div>
                      <div className="circle bg-[#33B679]"></div>
                      <div className="circle bg-[#0B8043]"></div>
                      <div className="circle bg-[#039BE5]"></div>
                      <div className="circle bg-[#3F51B5]"></div>
                      <div className="circle bg-[#7986CB]"></div>
                      <div className="circle bg-[#616161]"></div>
                      <div className="circle bg-[#9E69AF]"></div>
                      </div>

                      
                      <AutoCompleteCE/>
                                           

                      <div className="mt-9">
                        <SliderFG/>  
                      </div> 
                      
                      </div>
                      {/* Move TimeBubble to the right side */}
                      <div className="justify-end mt-9 ml-5">
                        <TimeBubble />
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