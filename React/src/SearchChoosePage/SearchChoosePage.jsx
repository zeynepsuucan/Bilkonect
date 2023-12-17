import React from "react";
import "./SearchChoosePageStyle.css";

import LeftBar from '../SideBarComponents/LeftBar.jsx';
import RightBar from '../SideBarComponents/RightBar.jsx';

import SaleCreate from '../CreatePostComponents/SaleCreate.jsx';
import IMGCreate from '../CreatePostComponents/IMGCreate.jsx';
import TripCreate from '../CreatePostComponents/TripCreate.jsx';
import TextCreate from '../CreatePostComponents/TextCreate.jsx';

import {useNavigate, useParams} from "react-router-dom";

const SearchChoosePage = () => {

    const navigate = useNavigate();


    const profileClicker = (event) => {
        event.preventDefault();

        navigate("/searchProfiles")
    
    }

    const postClicker = (event) => {
        event.preventDefault();

        navigate("/searchPosts")

    }

  return (

    <div className="outer-frame">
        <div>
      < LeftBar/>
      </div>
      
        <div className="search-choose-frame">
      <div className="div">
        <p className="text-wrapper">What would you like to search?</p>
        <div className="overlap">
          <div className="group">
            <div className="overlap-group-wrapper">
              <div className="overlap-group">
                <div className="profiles" onClick={profileClicker}>Profiles </div>
              </div>
            </div>
          </div>
          <div className="group-wrapper">
            <div className="overlap-group-wrapper">
              <div className="overlap-group">
                <div className="posts" onClick={postClicker}>Posts</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
      
      <div>
        <RightBar/>
      </div>
      </div>


  );
};

export default SearchChoosePage;
