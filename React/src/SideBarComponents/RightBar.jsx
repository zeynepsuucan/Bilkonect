import React, {useEffect, useState} from "react";
import "./RightBarStyle.css";
import pfpIMG from "./image 37.png"
import polyIMG from "./Polygon 3.png"

import {useNavigate} from "react-router-dom";

const RightBar = () => {

  const navigate = useNavigate();

  const username = sessionStorage.getItem("username");

  const profileClickHandler = (event) => {
    event.preventDefault();

    navigate("/ownProfile")
  }

  const studentClick = (event) => {
    event.preventDefault();

    navigate("/studentPage");
  }

  const [followers, setFollowers] = useState();
  const [followings, setFollowings] = useState();
  const [pp, setPp] = useState();

  useEffect(() => {
    fetch("http://localhost:5000/getProfile/"+ sessionStorage.getItem("username") +"", {
      method: "GET",
    })
      .then((response) => {
        console.log(response);
        return response.json();
      })
      .then((text) => {
        setFollowers(text.followers);
        setFollowings(text.following);
        setPp(text.pp);
      })
      .catch((err) => console.log(err));
  }, []);
    
  return (
    <div className="right-bar-frame">
      <div className="div">
        <div className="overlap-group-bar2">
          <div className="overlap">
            <img className="image" alt="Image" src= {pfpIMG} />
          </div>
          <div className="text-wrapper-po" >profile</div>
          <img className="polygon" alt="Polygon" src= {polyIMG} />
        </div>
        <div className="overlap-2">
          <div className="text-wrapper-2" onClick={studentClick}>student page</div>
          <div className="text-wrapper-3">{username}</div>
          <div className="followers-following">
           {followers} followers
            <br />
           {followings} following
          </div>
          <div className="facetune" style= {{backgroundImage: 'url(' + pp + ')'}} />
          <div className="text-wrapper-4"onClick={profileClickHandler}>go to profile</div>
        </div>
      </div>
    </div>
  );
};

export default RightBar;
