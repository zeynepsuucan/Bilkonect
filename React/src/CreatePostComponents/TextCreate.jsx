import React, {useState} from "react";
import "./TextCreateStyle.css";

import {useNavigate} from "react-router-dom";

const TextCreate = (props) => {

    const navigate= useNavigate();
    const [title, set_title] = useState("");
    const [description, set_description] = useState("");

    const createHandler = (event) => {
      

      fetch("http://localhost:5000/" + props.post_type +"", 
    {
      method: "POST",
      headers: {
        "content-type": "application/json"
      },
      body: JSON.stringify({
          title: title,
          description: description, 
          post_type: props.post_type,
          owner: sessionStorage.getItem("username"),
          criteria: "Fitness partner",
          share_date: "2023-12-31T12:00:00",
                          })
    }
    )
    .then(response => response.json())
    .catch(err=> console.log(err))

    navigate("/postspage");
  };

  return (
    <div className="text-create">
      <div className="overlap-group-wrapper">
        <div className="overlap-group">
         
          <input className="rectangle" 
            type="text" 
            value = {title}
            placeholder="Enter your title here..."
            onChange = {(e) => set_title(e.target.value)}
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

export default TextCreate;