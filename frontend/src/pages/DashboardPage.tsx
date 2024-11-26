import React from 'react'
import '../DashboardPage.css';
import Navbar from '../components/Navbar';
import SwitchWQ from '../components/SwitchWQ';

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
                    
                    <div className='pt-44'>
                      <SwitchWQ/>
                    </div>
                    
                </div>
            </div>
        </div>
    </>  
    
  )
}

export default DashboardPage