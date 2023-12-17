import React, {useState, useEffect} from "react";
import "./ChatPrevStyle.css";

import {useNavigate} from "react-router-dom";


const ChatPrev = (props) => {
    

    const navigate = useNavigate();
    const [image, setImage] = useState("");

    const clickHandler = (event) => {
        event.preventDefault();
        navigate("/chats/" + props.chat_id + "")
        
    }

    useEffect(() => {
      fetch("http://localhost:5000/getProfile/"+ props.username + "", {
        method: "GET",
      })
        .then((response) => {
          return response.json();
        })
        .then((text) => {
          setImage(text.pp)
          
        })
        .catch((err) => console.log(err));
  
      }, []);

    return (
      <div className="chat-prev-frame" onClick={clickHandler}>

       <div className = "profile-container">
        <div className="facetune-pfp" style = {{backgroundImage: 'url(' + image  + ')'}} />

        <div className="text-wrapper-mini"> {props.username}  </div>

        <div className="last-message-wrapper">  "{props.lastMessage}"</div>

        </div>

       </div> 

       

    );
  };

  export default ChatPrev;
  