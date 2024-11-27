import React from 'react';
import '../LandingPage.css';
import RollCallIcon from "../assets/RollCallIcon.png";
import GoogleIcon from "../assets/GoogleIcon.png"
import GoogleLogo from "../assets/googleLogo.svg"
import { IconButton } from '@mui/material';

const roll = " Roll "

const LandingPage = () => {
  
  // const signup = async () => {
  //   window.location.href = 'http://localhost:5000/auth/signup';
  // };

  const login = async () => {
    window.location.href = 'http://localhost:5000/auth/login';
  };



  return (
    <>
      <div className="flex w-full">
        <div className="container-left">
          <div className="header-text">
            <span>Welcome to </span>
            <span className="header-text-bold">Roll Call</span>
          </div>

          <div className="paragraph">
            Your Personal Daily Brief — Transforming Your Google
          </div>
          <div className="paragraph">
            Calendar into Clarity.
            <span className="paragraph-bold">
              {roll}
            </span>
            into Your Day with Confidence.
          </div>

          <div className="rollcall-logo-image-container">
            <img src={RollCallIcon} alt="" />
          </div>
        </div>

        <div className="container-right">
          <div className="login-text pb-3">
             Ready for your roll call?
          </div>
          <button onClick={login}className="log-in">
            <img src={GoogleLogo} />
          </button>

        </div>
      </div>
    </>
  );
}

export default LandingPage;
