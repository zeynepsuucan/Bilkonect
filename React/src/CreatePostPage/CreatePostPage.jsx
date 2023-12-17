import React from "react";
import "./CreatePostPageStyle.css";
import LeftBar from '../SideBarComponents/LeftBar.jsx';
import RightBar from '../SideBarComponents/RightBar.jsx';

import SaleCreate from '../CreatePostComponents/SaleCreate.jsx';
import IMGCreate from '../CreatePostComponents/IMGCreate.jsx';
import TripCreate from '../CreatePostComponents/TripCreate.jsx';
import TextCreate from '../CreatePostComponents/TextCreate.jsx';

import {useNavigate, useParams} from "react-router-dom";


const CreatePostPage = () => {

  const {postType} = useParams();

    const navigate = useNavigate();

    const renderPostComponent = () => {
      switch (postType) {
        case "DonationPost" :
        case  "LostPost":
        case "FoundPost":
  
          return (
            <IMGCreate
             post_type = {postType}
            />
            
          );
        case "SecondHandSalePost":
          
          return (
            <SaleCreate
           
            />
          );
        case "NeedPost":
        case "CourseMaterialPost":
        case "StudyBuddyPost":
        case "GymBuddyPost":
        case "RoomMatePost":
          return (
            <TextCreate
            post_type = {postType}
            />
          );
        case "TripBuddyPost":
          return (
            <TripCreate
            
            />
          );
        
        default:
          return null;
      }
    };


    return (
      <div className="create-frame">
        <div>
      < LeftBar/>
      </div>
      
      <div className="mid-frame"> 
        <div className = "create-post-text">Create a Post!</div>
         <div className="post-review">
         {
              <div className= "content" >
                {renderPostComponent(postType)}
              </div>
            }
          
         </div>
      
     </div>
      
      <div>
        <RightBar/>
      </div>
      </div>

      
    );

  };

  export default CreatePostPage;
  