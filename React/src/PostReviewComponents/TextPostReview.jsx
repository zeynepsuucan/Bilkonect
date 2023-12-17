import React, {useState, useEffect} from "react";
import "./TextPostReviewStyle.css";
import rectangleIMG from "./Rectangle 32.png"
import contentIMG from "./image 33.png"
import imageX from "./image 34.png"
import favIMG from "./favorite 2.png"
import {useNavigate} from "react-router-dom";

const TextPostReview = (props) => {

  const navigate = useNavigate();
  const [_chat, _setChat] = useState("Chat");


  useEffect(() => {

    if(props.owner == sessionStorage.getItem("username")){
      _setChat("Reviewing your post")
    }
    else{
      
    }

  }, [])

  const chatClickHandler = (event) => {

    if(props.owner == sessionStorage.getItem("username")){

    }
    else{

      fetch("http://localhost:5000/checkexistance", 
        {
          method: "POST",
          headers: {
            "content-type": "application/json"
          },
          body: JSON.stringify({
              username: sessionStorage.getItem("username"),
              post_id: props.post_id
              
                              })
        }
        )

        .then((response) => {
          return response.json();
        })
        .then((text) => {

          if(text.result === "True"){
            navigate("/chats/" + text.return_chat_id + "")
          }
          else{
            chatCreator();
          }
        
        })

        .catch(err=> console.log(err))
      }
  }

  const chatCreator = () => {

    fetch("http://localhost:5000/create_chat", 
      {
        method: "POST",
        headers: {
          "content-type": "application/json"
        },
        body: JSON.stringify({
            sender_username: sessionStorage.getItem("username"),
            receiver_username: props.owner,
            post_id: props.post_id
                            })
      }
      )

      .then((response) => {
        return response.json();
      })
      .then((text) => {
        navigate("/chats/" + text.message +"") 
      })

      .catch(err=> console.log(err))
  }

  return (
    <div className="text-post-review-frame">
      <div className="overlap-group-wrapper">
        <div className="overlap-group">
          <div className="text-wrapper">By {props.owner}</div>
          <div className="div">Favorite Post</div>
          <div className="text-wrapper-2">{props.description}</div>
          <div className="text-wrapper-3">{props.title}</div>
          <div className="overlap">
            <div className="send-request-to-chat" onClick= {chatClickHandler}>{_chat} </div> 
          </div>
          <img className="favorite" alt="Favorite" src={favIMG} />
          <img className="img" alt="Image" src={imageX} />
        </div>  
      </div>
    </div>
  );
};

export default TextPostReview;