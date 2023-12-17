import React, {useState, useEffect} from "react"
import "./StudentPageStyle.css"
import LeftBar from "../SideBarComponents/LeftBar.jsx";
import RightBar from "../SideBarComponents/RightBar.jsx";
import IMGPost from "../PostComponents/IMGPost.jsx";
import SalePost from "../PostComponents/SalePost.jsx";
import TextPost from "../PostComponents/TextPost.jsx";
import TripPost from "../PostComponents/TripPost.jsx";


const StudentPage = () => {

    const [posts, setPosts] = useState([])

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

    useEffect(() => {
        fetch("http://localhost:5000/studentpage/" + sessionStorage.getItem("username"), {
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

    return (
        <div className="student-page-frame">
          <div>
            <LeftBar />
          </div>
    
          <div className="student-page-mid-frame">
            <p className="student-page-header">Posts in student page</p>
            <div className="student-page-post-review">   
              {posts &&
               posts.map((post) => {
                return(
                  <div key={post.id}>
                    {renderPostComponent(post)}
                  </div>
                )
                    
                })}
            </div>
          </div>
    
          <div>
            <RightBar />
          </div>
        </div>
      );




}

export default StudentPage;