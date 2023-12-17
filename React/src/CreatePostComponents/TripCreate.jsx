import React, {useState} from "react";
import "./TripCreateStyle.css";
import {useNavigate} from "react-router-dom";

const TripCreate = () => {

  const navigate= useNavigate();

    const today = new Date();
    const [title, set_title] = useState("");
    const [description, set_description] = useState("");
    const [from, set_from] = useState("");
    const [to, set_to] = useState("");
    const [when, set_when] = useState("");


    const createHandler = (event) => {
        event.preventDefault();
        fetch("http://localhost:5000/TripBuddyPost", 
      {
        method: "POST",
        headers: {
          "content-type": "application/json"
        },
        body: JSON.stringify({
                            title: title,
                            description: description,
                            post_type:  "TripBuddyPost",
                            owner: sessionStorage.getItem("username"),
                            criteria: "Travel Companion",
                            isArchived: false,
                            share_date: "2023-12-31T12:00:00",
                            tripDate: when,
                            destination: to,
                            departure: from
                            })
      }
      )
      .then(response => response.json())
      .catch(err=> console.log(err))

      navigate("/postspage");
      };
    

  return (
    <div className="trip-create">
      <div className="overlap-group-wrapper">
        <div className="overlap-group">
          <input className="rectangle" 
            type="text" 
            value = {title}
            placeholder="Enter your title here..."
            onChange = {(e) => set_title(e.target.value)}
          />

          <div className="text-wrapper">From:</div>
          <input className="img" 
            type="text" 
            value = {from}
            
            onChange = {(e) => set_from(e.target.value)}
          />

          <div className="text-wrapper-to">To:</div>
          <input className="img2" 
            type="text" 
            value = {to}
            
            onChange = {(e) => set_to(e.target.value)}
          />

          <div className="text-wrapper-when">When:</div>
          <input className="img3" 
            type="text" 
            value = {when}
            
            onChange = {(e) => set_when(e.target.value)}
          />  

          <div className="overlap">
            <div className="text-wrapper-2"onClick = {createHandler}>create post</div>
          </div>
          <div className="text-wrapper-3">Add a description:</div>

          <textarea className="rectangle-2" 
            type="text" 
            placeholder="Enter your description here..."
            value = {description}
            onChange = {(e) => set_description(e.target.value)}
          />
          <div className="text-wrapper-4">Add title:</div>
          <img className="image" alt="Image" src="https://c.animaapp.com/EmWF9VUV/img/image-39@2x.png" />
        </div>
      </div>
    </div>
  );
};

export default TripCreate;