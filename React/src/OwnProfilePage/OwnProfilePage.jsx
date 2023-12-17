import React, {useState, useEffect} from "react";
import "./OwnProfilePageStyle.css";

import LeftBar from '../SideBarComponents/LeftBar.jsx';
import RightBar from '../SideBarComponents/RightBar.jsx';

import Star from './star 9.png';
import Fav from './favorite 2.png';

import DonationPostReview from '../PostReviewComponents/DonationPostReview.jsx';
import SalePostReview from '../PostReviewComponents/SalePostReview.jsx';
import TextPostReview from '../PostReviewComponents/TextPostReview.jsx';
import TripPostReview from '../PostReviewComponents/TripPostReview.jsx';

import IMGPost from '../PostComponents/IMGPost.jsx';
import SalePost from '../PostComponents/SalePost.jsx';
import TextPost from '../PostComponents/TextPost.jsx';
import TripPost from '../PostComponents/TripPost.jsx';

import ProfileLeftBar from '../ProfileSideBarComponents/ProfileLeftBar.jsx';
import ProfileRightBar from '../ProfileSideBarComponents/ProfileRightBar.jsx';

import {useNavigate} from "react-router-dom";


const OwnProfilePage = () => {

  const [posts, setPosts] = useState([]);
  const [followers, setFollowers] = useState();
  const [followings, setFollowings] = useState();
  const [pp, setPp] = useState();

  useEffect(() => {
    fetch("http://localhost:5000/getPosts/"+ sessionStorage.getItem("username") +"", {
      method: "GET",
    })
      .then((response) => {
        return response.json();
      })
      .then((text) => {
        setPosts(text);
      })
      .catch((err) => console.log(err));
    }, []);

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

    // const navigate = useNavigate();

    // const clickHandler1 = (event) => {
    // event.preventDefault();
    // navigate("/");
    // }

    // const clickHandler2 = (event) => {
    // event.preventDefault();
    // navigate("/homepage");
    // }


    const renderPostComponent = (post) => {
      switch (post.post_type) {
        case "DonationPost" :
        case  "LostPost":
        case "FoundPost":
          return (
            <IMGPost
              owner={post.owner}
              description={post.description}
              title={post.title}
              image={post.image}
              id= {post.post_id}
              // Additional props specific to DonationPost
            />
          );
        case "SecondHandSalePost":
          
          return (
            <SalePost
              owner={post.owner}
              description={post.description}
              title={post.title}
              price = {post.price}
              image = {post.image}
              id= {post.post_id}
              // Additional props specific to SalePost
            />
          );
        case "NeedPost":
        case "CourseMaterialPost":
        case "StudyBuddyPost":
        case "GymBuddyPost":
        case "RoomMatePost":
          return (
            <TextPost
              owner={post.owner}
              description={post.description}
              title={post.title}
              id= {post.post_id}
              // Additional props specific to TextPost
            />
          );
        case "TripBuddyPost":
          return (
            <TripPost
              owner={post.owner}
              description={post.description}
              title={post.title}
              departure={post.departure}
              destination={post.destination}
              tripDate={post.tripDate}
              id= {post.post_id}
              // Additional props specific to TripPost
            />
          );
        
        default:
          return null;
      }
    };


    return (
      <div className="own-profile-frame">
        <div>
      < ProfileLeftBar/>
      </div>
      
      <div className="mid-frame"> 

      <div className="profile-props2">
        <div className="text-wrapper-pfp2"> {sessionStorage.getItem("username")} </div>
        <div className="overlap-group-pfp2">
            
          <div className="text-wrapper-2-pfp2"> {followings} following</div>
          <div className="text-wrapper-3-pfp2">rate:</div>
          <div className="text-wrapper-4-pfp2"> {followers} followers</div>

          <div className="line" alt="Line" />
          
          <div className="group">
            <img className="star" alt="Star" src={Star} />
            <img className="img-pfp" alt="Star" src={Star} />
            <img className="star-2" alt="Star" src={Star} />
            <img className="star-3" alt="Star" src= {Star} />
            <img className="favorite" alt="Favorite" src= {Fav} />
          </div>

        </div>

        <div className="facetune-pfp" style= {{backgroundImage: 'url(' + pp + ')'}} />
      </div>

      <div className="profile-posts" >
      {posts &&
            posts.map((post) => (
              <div key={post.id}>
                {renderPostComponent(post)}
              </div>
            ))}
      </div>
      
      </div>
      
      <div>
        <ProfileRightBar/>
      </div>
      </div>
    );
  };

  export default OwnProfilePage;
  