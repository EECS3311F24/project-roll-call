import React from 'react'
import '../DashboardPage.css';
import Navbar from '../components/Navbar';
import GreetingsSett from '../components/GreetingsSett';

const DashboardPage = () => {
  return (
    <>
        <div className="flex flex-col min-w-[800px] bg-custombg">
            <Navbar />
            <div className="container">
                <div className="container-center">
                    <div className="heading-text">
                    Sara's Dashboard
                    <GreetingsSett/>
                    </div>
                </div>
            </div>
        </div>
    </>  
    
  )
}

export default DashboardPage