import React from "react";
import "./ProfileRightBarStyle.css";

import backIMG from "./undo 2.png";
import { useNavigate } from "react-router-dom";

const ProfileRightBar = () => {

  const navigate = useNavigate();

  const editHandler = (event) => {
    event.preventDefault();

    navigate("/editOwnProfile");
  }

  const backHandler = (event) => {
    event.preventDefault();

    navigate("/postspage")
  }

  return (
    <div className="profile-right-frame">
      <div className="div">
        <div className="overlap-group">
          
        </div>
        <div className="overlap-2">

          <div className="text-wrapper-3" onClick= {backHandler}>go back</div>

          <img className="facetune" src= {backIMG} onClick={backHandler}/>
          <div className="text-wrapper-4" onClick={editHandler}>edit profile</div>
        </div>
      </div>
    </div>
  );
};
export default ProfileRightBar;

