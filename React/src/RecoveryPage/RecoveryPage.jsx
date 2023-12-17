import React, {useState} from "react";
import "./RecoveryPageStyle.css";
import {useNavigate} from "react-router-dom";

const RecoveryPage = () => {

    const navigate = useNavigate();

    const clickHandler1 = (event) => {
        event.preventDefault();
        // alert("Hello!");
        navigate("/login");
      }

    return (
      <div className="element-recovery-page">
        <div className="overlap-group-wrapper">
          <div className="overlap-group">
            <div className="overlap">
              <div className="div">
                <input className="rectangleInput" />
                <div className="text-wrapper">Email address</div>
                <div className="recover-password-wrapper">
                  <img
                    className="recover-password"
                    alt="Recover password"
                    src="https://c.animaapp.com/zJ4IjWpe/img/recover-password.png"
                  />
                </div>
                <img className="image" alt="Image" src="https://c.animaapp.com/zJ4IjWpe/img/image-32@2x.png" />
              </div>
              <div className="text-wrapper-2">Recover your password</div>
              <p className="go-back-to-log-in">
                <span className="span">Go back to </span>
                <span className="text-wrapper-3" onClick= {clickHandler1} >Log in</span>
              </p>
            </div>
            <div className="div-wrapper">
              <div className="text-wrapper-4">Bilkonect</div>
            </div>
          </div>
        </div>
      </div>
    );
  };

export default RecoveryPage;
  