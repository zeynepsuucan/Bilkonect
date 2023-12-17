import React, {useState, useEffect} from "react";
import "./ProfilePageStyle.css";
import {useParams} from "react-router-dom";

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

import {useNavigate} from "react-router-dom";


const ProfilePage = () => {

  const {username} = useParams();
  const [_follow, _setFollow] = useState("");

  const [posts, setPosts] = useState([]);
  const [followers, setFollowers] = useState();
  const [followings, setFollowings] = useState();
  const [pp, setPp] = useState();
  
  const followHandler = () => {

    if(_follow == "Follow"){

      fetch("http://localhost:5000/follow", 
      {
        method: "POST",
        headers: {
          "content-type": "application/json"
        },
        body: JSON.stringify({
            follower_name: sessionStorage.getItem("username"),
            followed_name: username
                            })
      }
      )
      .then((response) => {
        return response.json();
      })
      .then((text) => {
      })

      .catch(err=> console.log(err))

      _setFollow("Following")
    }
    else{
    
      fetch("http://localhost:5000/follow", 
      {
        method: "DELETE",
        headers: {
          "content-type": "application/json"
        },
        body: JSON.stringify({
            follower_name: sessionStorage.getItem("username"),
            followed_name: username
                            })
      }
      )
      .then((response) => {
        return response.json();
      })
      .then((text) => {
      })

      .catch(err=> console.log(err))

      _setFollow("Follow")
    }
    
  }


  useEffect(() => {
    fetch("http://localhost:5000/getPosts/"+ username +"", {
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
    fetch("http://localhost:5000/getProfile/"+ username +"", {
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



      fetch("http://localhost:5000/checkfollows", 
      {
        method: "POST",
        headers: {
          "content-type": "application/json"
        },
        body: JSON.stringify({
            followerName: sessionStorage.getItem("username"),
            followedName: username
                            })
      }
      )
      .then((response) => {
        return response.json();
      })
      .then((text) => {

        if(text.follows == "False"){
          _setFollow("Follow")
        }
        else if (text.follows == "True"){
          _setFollow("Following")
        }
      })

      .catch(err=> console.log(err))

  }, [_follow]);


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
      <div className="profile-frame">
        <div>
      < LeftBar/>
      </div>
      
      <div className="mid-frame"> 

      <div className="profile-props">
        <div className="text-wrapper-pfp"> {username} </div>
        <div className="overlapp">
            <div className="follow" onClick= {followHandler}> {_follow} </div> 
        </div>
        <div className="overlap-group-pfp">
            
          <div className="text-wrapper-2-pfp"> {followings} following</div>
          <div className="text-wrapper-3-pfp">rate:</div>
          <div className="text-wrapper-4-pfp"> {followers} followers</div>

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
        <RightBar/>
      </div>
      </div>
    );
  };

  export default ProfilePage;
  