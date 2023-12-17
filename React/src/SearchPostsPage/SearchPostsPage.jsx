import React, {useState, useEffect} from "react";
import "./SearchPostsPageStyle.css";
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


const SearchPostsPage = () => {

  const [posts, setPosts] = useState([]);
  const [input, setInput] = useState();


    const Searcher = (e) => {
        setInput(e.target.value);
    }

  
  useEffect(() => {
    fetch("http://localhost:5000/searchByTitle/"+ input +"", {
      method: "GET",
    })
      .then((response) => {
        return response.json();
      })
      .then((text) => {
        setPosts(text);
      })
      .catch((err) => console.log(err));
    }, [input]);


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
          case "RoommatePost":
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
        <div className="search-post-frame">
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

  export default SearchPostsPage;
  