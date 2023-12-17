import React, {useState} from "react";
import "./CreateChoosePageStyle.css";
import LeftBar from '../SideBarComponents/LeftBar.jsx';
import RightBar from '../SideBarComponents/RightBar.jsx';
import SaleCreate from '../CreatePostComponents/SaleCreate.jsx';
import IMGCreate from '../CreatePostComponents/IMGCreate.jsx';
import TripCreate from '../CreatePostComponents/TripCreate.jsx';
import TextCreate from '../CreatePostComponents/TextCreate.jsx';

import {useNavigate} from "react-router-dom";


const CreateChoosePage = () => {

    const options = [
        {label: "Second Hand Sale Post", value: "SecondHandSalePost"},
        {label: "Donation Post", value: "DonationPost"},
        {label: "Lost Post", value: "LostPost"},
        {label: "Found Post", value: "FoundPost"},
        {label: "Need Post", value: "NeedPost"},
        {label: "GymBuddy Post", value: "GymBuddyPost"},
        {label: "RoomMate Post", value: "RoomMatePost"},
        {label: "TripBuddy Post", value: "TripBuddyPost"},
        {label: "Course Material Post", value: "CourseMaterialPost"},
        {label: "StudyBuddy Post", value: "StudyBuddyPost"},
      ]

    const [postType, setPostType] = useState("SecondHandSalePost");
  
    const navigate = useNavigate();

    
    const clickHandler = (event) => {
    event.preventDefault();
    navigate(`/createPostPage/${postType}`);
    }

    return (
      <div className="create-choose-frame">
        <div>
      < LeftBar/>
      </div>
      
      <div className="mid-frame"> 
        <div className = "create-post-text">Create a Post!</div>
         <div className="choose-div"> 
          <div className ="text-select"> Select Post Type </div>
           <select className="selector" onChange = { (e) => setPostType(e.target.value)}> 
                {options.map(option => (
                  <option value={option.value}>{option.label}</option>
                ))}
                </select>
        </div>
      <div className="cont-wrapper" onClick={clickHandler}>Continue </div> 
     </div>
      
      <div>
        <RightBar/>
      </div>
      </div>
    );
  };

  export default CreateChoosePage;
  