import React, { useEffect, useState } from "react";
import "./PostsPageStyle.css";
import LeftBar from "../SideBarComponents/LeftBar.jsx";
import RightBar from "../SideBarComponents/RightBar.jsx";

import DonationPostReview from "../PostReviewComponents/DonationPostReview.jsx";
import SalePostReview from "../PostReviewComponents/SalePostReview.jsx";
import TextPostReview from "../PostReviewComponents/TextPostReview.jsx";
import TripPostReview from "../PostReviewComponents/TripPostReview.jsx";

import IMGPost from "../PostComponents/IMGPost.jsx";
import SalePost from "../PostComponents/SalePost.jsx";
import TextPost from "../PostComponents/TextPost.jsx";
import TripPost from "../PostComponents/TripPost.jsx";

import { useNavigate } from "react-router-dom";

const PostsPage = () => {
  const [posts, setPosts] = useState([]);

  const options = [
    {label: "Any", value: "feed/" + sessionStorage.getItem("username") + ""},
    {label: "Second Hand Sale Post", value: "getsecond"},
    {label: "Donation Post", value: "getdonation"},
    {label: "Lost Post", value: "getlost"},
    {label: "Found Post", value: "getfound"},
    {label: "Need Post", value: "getneed"},
    {label: "GymBuddy Post", value: "getgym"},
    {label: "RoomMate Post", value: "getroom"},
    {label: "TripBuddy Post", value: "gettrip"},
    {label: "Course Material Post", value: "getcourse"},
    {label: "StudyBuddy Post", value: "getstudy"},
  ]

  const [postType, setPostType] = useState("feed/" + sessionStorage.getItem("username") + "");

  useEffect(() => {
    fetch("http://localhost:5000/" + postType , {
      method: "GET",
    })
      .then((response) => {
        return response.json();
      })
      .then((text) => {
        setPosts(text);
      })
      .catch((err) => console.log(err));
  }, [postType]);

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
    <div className="posts-frame">
      <div>
        <LeftBar />
      </div>

      <div className="mid-frame">
        <div className="wrapper">
      
        <div className ="text-select"> Filter Post Type: </div>
           <select className="selector" onChange = { (e) => setPostType(e.target.value)}> 
                {options.map(option => (
                  <option value={option.value}>{option.label}</option>
                ))}
                </select>
        </div>        

        <div className="post-review">
          {posts &&
            posts.map((post) => (
              <div key={post.id}>
                {renderPostComponent(post)}
              </div>
            ))}
        </div>
      </div>

      <div>
        <RightBar />
      </div>
    </div>
  );
};

export default PostsPage;