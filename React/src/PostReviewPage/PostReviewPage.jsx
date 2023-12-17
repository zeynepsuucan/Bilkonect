import React, {useState, useEffect} from "react";
import {useParams} from "react-router-dom";
import "./PostReviewPageStyle.css";
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


const PostReviewPage = () => {

    // const navigate = useNavigate();

    // const clickHandler1 = (event) => {
    // event.preventDefault();
    // navigate("/");
    // }

    // const clickHandler2 = (event) => {
    // event.preventDefault();
    // navigate("/homepage");
    // }

    const [posts, setPosts] = useState([]);
    const [post, setPost] = useState(null);

    const {post_id} = useParams();

  useEffect(() => {
    fetch("http://localhost:5000/getPostFromID/"+ post_id +"", {
      method: "GET",
    })
      .then((response) => {
        return response.json();
      })
      .then((text) => {
        setPost(text);
      })
      .catch((err) => console.log(err));
  }, []);

  const renderPostComponent = (post) => {
    switch (post.post_type) {
      case "DonationPost" :
      case  "LostPost":
      case "FoundPost":

      console.log("this is good");
        return (
          <DonationPostReview
            post_id={post.post_id}
            owner={post.owner}
            description={post.description}
            title={post.title}
            image={post.image}
            // Additional props specific to DonationPost
          />
          
        );
      case "SecondHandSalePost":
        
        return (
          <SalePostReview
          post_id={post.post_id}
            owner={post.owner}
            description={post.description}
            title={post.title}
            price = {post.price}
            image = {post.image}
            // Additional props specific to SalePost
          />
        );
      case "NeedPost":
      case "CourseMaterialPost":
      case "StudyBuddyPost":
      case "GymBuddyPost":
      case "RoomMatePost":
        return (
          <TextPostReview
          post_id={post.post_id}
            owner={post.owner}
            description={post.description}
            title={post.title}
            // Additional props specific to TextPost
          />
        );
      case "TripBuddyPost":
        return (
          <TripPostReview
            post_id={post.post_id}
            owner={post.owner}
            description={post.description}
            title={post.title}
            departure={post.departure}
            destination={post.destination}
            tripDate={post.tripDate}
            // Additional props specific to TripPost
          />
        );
      
      default:
        return null;
    }
  };

  return (
    <div className="postrev-frame">
      <div>
        <LeftBar />
      </div>

      <div className="mid-frame">
        <div className="post-review">
          {post &&
              <div className= "content" key={post.id}>
                {renderPostComponent(post)}
              </div>
            }
        </div>
      </div>

      <div>
        <RightBar />
      </div>
    </div>
  );
  };

  export default PostReviewPage;
  