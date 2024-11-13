import React from 'react';
import '../LandingPage.css';
import RollCallIcon from "../assets/RollCallIcon.png";
import GoogleIcon from "../assets/GoogleIcon.png"
import { IconButton } from '@mui/material';

const roll = " Roll "

const LandingPage = () => {
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
            Login into your account
          </div>
          <button className="log-in">
            <img src={GoogleIcon} alt="" className="icon" />
            Log in
          </button>

          <div className="sign-up-text pt-20 pb-3">
            New here?
          </div>
          <button className="sign-up">
            <img src={GoogleIcon} alt="" className="icon" />
            Sign up with Google
          </button>
        </div>
      </div>
    </>
  );
}

export default LandingPage;
