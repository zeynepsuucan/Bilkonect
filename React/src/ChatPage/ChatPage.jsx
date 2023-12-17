import React, {useState, useEffect} from "react";
import "./ChatPageStyle.css";

import ChatBox from "../ChatComponents/ChatBox.jsx"

import LeftBar from '../SideBarComponents/LeftBar.jsx';
import RightBar from '../SideBarComponents/RightBar.jsx';
import { useParams } from "react-router-dom";

const ChatPage = () => {

    const {chat_id} = useParams();

    const[post_id, set_post_id] = useState("");
    const[other_user,set_other_user] = useState("");
    

    useEffect(() => {

      fetch("http://localhost:5000/get_other_user", 
      {
        method: "POST",
        headers: {
          "content-type": "application/json"
        },
        body: JSON.stringify({
            username: sessionStorage.getItem("username"),
            chat_id: chat_id
            
                            })
      }
      )

      .then((response) => {
        return response.json();
      })
      .then((text) => {
        set_post_id(text.post_id);
        set_other_user(text.other_username);
      })

      .catch(err=> console.log(err))

    }, [])

  return (

    <div className="outer-chat-frame">
        <div>
      < LeftBar/>
      </div>
      <div className="mid-frame">
       <div className= "chat-bar-frame">

              <div >
              <ChatBox
               chat_id= {chat_id}
               post_id = {post_id}
               other_user = {other_user}
              />
              </div>
        </div>      

       </div> 
      
      <div>
        <RightBar/>
      </div>
      </div>


  );
};

export default ChatPage;
