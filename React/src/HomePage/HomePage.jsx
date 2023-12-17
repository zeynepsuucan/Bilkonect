import React from "react";
import "./HomePageStyle.css";
import LeftBar from '../SideBarComponents/LeftBar.jsx';
import RightBar from '../SideBarComponents/RightBar.jsx';

import DonationPostReview from '../PostReviewComponents/DonationPostReview.jsx';
import SalePostReview from '../PostReviewComponents/SalePostReview.jsx';
import TextPostReview from '../PostReviewComponents/TextPostReview.jsx';
import TripPostReview from '../PostReviewComponents/TripPostReview.jsx';

import IMGPost from '../PostComponents/IMGPost.jsx';
import SalePost from '../PostComponents/SalePost.jsx';
import TextPost from '../PostComponents/TextPost.jsx';
import TripPost from '../PostComponents/TripPost.jsx';

import {useNavigate} from "react-router-dom";


const HomePage = () => {

    // const navigate = useNavigate();

    // const clickHandler1 = (event) => {
    // event.preventDefault();
    // navigate("/");
    // }

    // const clickHandler2 = (event) => {
    // event.preventDefault();
    // navigate("/homepage");
    // }

    return (
      <div className="home-frame">
        <div>
      < LeftBar/>
      </div>
      
      <div className="mid-frame"> 

      <div className="post-review"> <SalePost/> </div>
      
      </div>
      
      <div>
        <RightBar/>
      </div>
      </div>
    );
  };

  export default HomePage;
  