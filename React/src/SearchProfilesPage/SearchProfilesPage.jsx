import React, {useState, useEffect} from "react";
import "./SearchProfilesPageStyle.css";
import LeftBar from '../SideBarComponents/LeftBar.jsx';
import RightBar from '../SideBarComponents/RightBar.jsx';

import img from './image 15.png';

import DonationPostReview from '../PostReviewComponents/DonationPostReview.jsx';
import SalePostReview from '../PostReviewComponents/SalePostReview.jsx';
import TextPostReview from '../PostReviewComponents/TextPostReview.jsx';
import TripPostReview from '../PostReviewComponents/TripPostReview.jsx';

import IMGPost from '../PostComponents/IMGPost.jsx';
import SalePost from '../PostComponents/SalePost.jsx';
import TextPost from '../PostComponents/TextPost.jsx';
import TripPost from '../PostComponents/TripPost.jsx';

import {useNavigate} from "react-router-dom";
import MiniProfile from "./MiniProfile.jsx";


const SearchProfilesPage = () => {

  const [users, setUsers] = useState([]);
  const [input, setInput] = useState();


    const Searcher = (e) => {
        setInput(e.target.value);
    }

  
  useEffect(() => {
    fetch("http://localhost:5000/getuserbyname/"+ input +"", {
      method: "GET",
    })
      .then((response) => {
        return response.json();
      })
      .then((text) => {
        setUsers(text);
      })
      .catch((err) => console.log(err));
    }, [input]);


    const renderProfileComponent = (user) => {

            return (
              <MiniProfile
                username={user.username}
                image={user.pp}
                // Additional props specific to TripPost
              />
            );
        
      };


    return (
        <div className="search-profile-frame">
        <div>
      < LeftBar/>
      </div>
      
      <div className="mid-frame"> 

      <div className="search-props2">
    
        <input type= "text" className="search-bar" 
        value = {input}
        onChange={Searcher}
        />
        <img className = "search-img" src={img}/>
          <div className="line" alt="Line" />
        
      </div>

      <div className="searched-posts" >
      {users &&
            users.map((user) => (
              <div key={user.bilkent_id}>
                {renderProfileComponent(user)}
              </div>
            ))}
      </div>
      
      </div>
      
      <div>
        <RightBar/>
      </div>
      </div>
    );
  };

  export default SearchProfilesPage;
  