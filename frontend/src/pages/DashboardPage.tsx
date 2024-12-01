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
                      </div>

                    <div className="columns">
                      <div className="left-column">
                        <div className="sub-heading-text ">
                          Customize your Greeting
                        </div > 

                        <SwitchWQ/>
                        
                        <div className="sub-heading-text ">
                          Classify your Calendar Events
                        </div > 
                        <div className="color-category">
                          <div className="color-stack">
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

                          <div className="category">
                            
                            <div className="sub-sub-heading-text ">
                              Category Type
                            </div > 
                            <AutoCompleteCE label="Category Type"/>
                            <AutoCompleteCE label="Category Type"/>
                            <AutoCompleteCE label="Category Type"/>
                            <AutoCompleteCE label="Category Type"/>
                            <AutoCompleteCE label="Category Type"/>
                            <AutoCompleteCE label="Category Type"/>
                            <AutoCompleteCE label="Category Type"/>
                            <AutoCompleteCE label="Category Type"/>
                            <AutoCompleteCE label="Category Type"/>
                            <AutoCompleteCE label="Category Type"/>
                            <AutoCompleteCE label="Category Type"/>
                          </div>

                          <div className="priority">
                            
                            <div className="sub-sub-heading-text ">
                              Priority
                            </div > 
                            <AutoCompleteCE label="Priority"/>
                            <AutoCompleteCE label="Priority"/>
                            <AutoCompleteCE label="Priority"/>
                            <AutoCompleteCE label="Priority"/>
                            <AutoCompleteCE label="Priority"/>
                            <AutoCompleteCE label="Priority"/>
                            <AutoCompleteCE label="Priority"/>
                            <AutoCompleteCE label="Priority"/>
                            <AutoCompleteCE label="Priority"/>
                            <AutoCompleteCE label="Priority"/>
                            <AutoCompleteCE label="Priority"/>
                          </div>
                        </div>
                      </div>    
                                          
                      <div className="right-column">
                        
                    <div className="sub-heading-text ">
                      Customize your Future at a Glance
                    </div >
                    
                    <div className="sub-sub-heading-text ">
                      Time frame in Weeks
                    </div >
                        <div className="slider">
                          <SliderFG/>  
                        </div> 

                        <SwitchPC/>
                        
                    <div className="sub-heading-text ">
                      Notification
                    </div >
                    
                    <div className="sub-sub-heading-text ">
                      Get your report emailed to you
                    </div >
                        <SwitchYesNo/> 
                        
                    <div className="sub-sub-heading-text ">
                      Set a time to receive your report
                    </div >   
                        </div>
                        <div className="time-bubble">
                          <TimeBubble />
                        </div>     
                      </div>
                    </div>

                    
                    
                    



                </div>
            </div>
    </>  
    
  )
}

export default DashboardPage