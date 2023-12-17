import React, {useState, useEffect} from "react";
import "./MiniProfileStyle.css";

import {useNavigate} from "react-router-dom";



const MiniProfile = (props) => {

    const navigate = useNavigate();

    const clickHandler = (event) => {
        event.preventDefault();

        if(sessionStorage.getItem("username") === props.username){
          navigate("/ownProfile/")
        }
        else {
          navigate("/visitProfile/" + props.username +"")
        }

        
    }

    return (
      <div className="mini-profile-frame" onClick={clickHandler}>

       <div className = "profile-container">
        <div className="facetune-pfp" style = {{backgroundImage: 'url(' + props.image  + ')'}} />

        <div className="text-wrapper-mini"> {props.username} </div>

        </div>

       </div> 

       

    );
  };

  export default MiniProfile;
  