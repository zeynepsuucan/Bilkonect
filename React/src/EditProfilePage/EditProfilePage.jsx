import React from "react";
import "./EditProfilePageStyle.css";
import ProfileLeftBar from '../ProfileSideBarComponents/ProfileLeftBar.jsx';
import ProfileRightBar from '../ProfileSideBarComponents/ProfileRightBar.jsx';

import SaleCreate from '../CreatePostComponents/SaleCreate.jsx';
import IMGCreate from '../CreatePostComponents/IMGCreate.jsx';
import TripCreate from '../CreatePostComponents/TripCreate.jsx';
import TextCreate from '../CreatePostComponents/TextCreate.jsx';

import {useNavigate, useParams} from "react-router-dom";
import EditProfileComponent from "./EditProfileComponent.jsx";


const EditProfilePage = () => {

  const {postType} = useParams();

    const navigate = useNavigate();

    return (
      <div className="proedit-frame">
        <div>
      < ProfileLeftBar/>
      </div>
      
      <div className="mid-frame"> 
        <div className = "proedit-post-text">Edit your profile:</div>
         <div className="post-review">
              <div className= "content" >
               <EditProfileComponent/>
              </div>
            
          
         </div>
      
     </div>
      
      <div>
        <ProfileRightBar/>
      </div>
      </div>

      
    );
};

  export default EditProfilePage;
  