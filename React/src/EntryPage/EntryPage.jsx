import React from "react";
import "./EntryPageStyle.css";
import {useNavigate} from "react-router-dom";
const EntryPage = () => {

  const navigate = useNavigate();

  const clickHandler1 = (event) => {
    event.preventDefault();
    navigate("/login");
  }

  const clickHandler2 = (event) => {
    event.preventDefault();
    navigate("/signup");
  }

  return (
    <div className="element-entry-page">
      <div className="div">
        <div className="overlap">
          <div className="text-wrapper">Bilkonect</div>
        </div>
        <div className="overlap-group" />
        <div className="overlap-2">
          <div className="div-wrapper">
            <div className="text-wrapper-2" onClick={clickHandler2}>Sign Up</div>
          </div>
          <div className="text-wrapper-3">don’t have an account?</div>
          <div className="text-wrapper-4">OR</div>
          <div className="login-wrapper">
            <div className="text-wrapper-7" onClick={clickHandler1}>Login</div>
          </div>
        </div>
        <div className="text-wrapper-5">Privacy policy</div>
        <div className="text-wrapper-6">Get Started !</div>
      </div>
    </div>
  );
};

export default EntryPage;
