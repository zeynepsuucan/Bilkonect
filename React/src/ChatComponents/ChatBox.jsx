import React, {useState, useEffect} from "react"
import {useParams} from "react-router-dom";
import ScrollToBottom from "react-scroll-to-bottom";
import "./ChatBoxStyle.css";


const ChatBox = (props) => {

    const [message, setMessage] = useState("");
    const [messageList, setMessageList] = useState([]);

    const[user_pp, set_user_pp] = useState("");
    const[post_title, set_post_title] = useState("");

    useEffect(() => {
      
        fetch("http://localhost:5000/getProfile/" + props.other_user + "", {
        method: "GET",
        })
        .then((response) => {
            return response.json();
        })
        .then((text) => {
            set_user_pp(text.pp);
        })
        .catch((err) => console.log(err));


        fetch("http://localhost:5000/get_messages/" + props.chat_id + "", {
            method: "GET",
        })
        .then((response) => {
            return response.json();
        })
        .then((text) => {
            setMessageList(text.messages);
        })
        .catch((err) => console.log(err));


      fetch("http://localhost:5000/getPostFromID/" + props.post_id + "", {
          method: "GET",
      })
      .then((response) => {
          return response.json();
      })
      .then((text) => {
          set_post_title(text.title);
      })
      .catch((err) => console.log(err));
    }, )

    const refresh = () => {
        fetch("http://localhost:5000/get_messages/" + props.chat_id + "", {
            method: "GET",
        })
        .then((response) => {
            return response.json();
        })
        .then((text) => {
            setMessageList(text.messages);
        })
        .catch((err) => console.log(err));
    }

    const sendMessage = (event) => {
        event.preventDefault();
        fetch("http://localhost:5000/send_message/"+ props.chat_id, 
      {
        method: "POST",
        headers: {
          "content-type": "application/json"
        },
        body: JSON.stringify({
            sender_name: sessionStorage.getItem("username"),
            content: message,
                            })
      }
      )
      .then(response => {response.json();
                        refresh();})
      .catch(err=> console.log(err))
    }

    return (
      <div className= "main-frame">
        <div className="chat-window">
        <div className="chat-header">
          <div className="title-post"> {post_title} </div>
          <div className="persona-wrap">
            <div className="info-user"> {props.other_user} </div>
            <div className="facetune-pfp" style = {{backgroundImage: 'url(' + user_pp  + ')'}} />
          </div>
        </div>
        <div className="chat-body">
            <ScrollToBottom className="message-container">
            {messageList && messageList.map((messageContent) => {
                return(
                <div
                  className="message"
                  id={ sessionStorage.getItem("username") === messageContent.sender_name ? "other" : "you"}
                >
                  <div>
                    <div className="message-content">
                      <p>{messageContent.content}</p>
                    </div>
                    <div className="message-meta">
                      <p id="author">{messageContent.sender_name}</p>
                    </div>
                  </div>
                </div> 
                )
            })}
            </ScrollToBottom>
        </div>
        <div className="chat-footer">
          <input
            type="text"
            value={message}
            placeholder="Write a message"
            onChange={(event) => {
              setMessage(event.target.value);
            }}
          />
          <button onClick={sendMessage}>&#9658;</button>
        </div>
      </div>     
      </div>
    )
}


export default ChatBox;