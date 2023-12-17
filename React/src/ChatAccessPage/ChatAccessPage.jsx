import React, {useState, useEffect} from "react";
import "./ChatAccessPageStyle.css";
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
import ChatPrev from "../ChatComponents/ChatPrev.jsx";


const ChatAccessPage = () => {

  const [chatInfos, setChatInfos] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/getallchats/"+ sessionStorage.getItem("username") + "", {
      method: "GET",
    })
      .then((response) => {
        return response.json();
      })
      .then((text) => {
        setChatInfos(text)
        
      })
      .catch((err) => console.log(err));

    }, []);


    const renderProfileComponent = (chatInfo) => {

            return (
              <ChatPrev
                username={chatInfo.username}
                chat_id={chatInfo.id}
                lastMessage={chatInfo.content}
    
              />
            );
        
      };


    return (
        <div className="chat-access-frame">
        <div>
      < LeftBar/>
      </div>
      
      <div className="mid-frame"> 

      <div className="search-props2">

      <div className = "ongoing-message" > Here are your ongoing chats: </div>
          <div className="line" alt="Line" />
        
      </div>

      <div className="searched-posts" >
      {chatInfos &&
            chatInfos.map((chatInfo) => (
              <div key={chatInfo.id}>
                {renderProfileComponent(chatInfo)}
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

  export default ChatAccessPage;
  