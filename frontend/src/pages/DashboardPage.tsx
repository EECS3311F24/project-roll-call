import React from 'react'
import '../DashboardPage.css';
import Navbar from '../components/Navbar';

const DashboardPage = () => {
  return (
    <>
        <div className="flex flex-col min-w-[800px] bg-custombg">
            <Navbar />
            <div className="container">
                <div className="container-center">
                    <div className="text">
                    Sara's Dashboard
                    </div>
                </div>
            </div>
        </div>
    </>  
    
  )
}

export default DashboardPage