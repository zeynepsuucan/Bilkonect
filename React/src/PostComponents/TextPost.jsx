import React from "react";
import "./TextPostStyle.css";
import {useNavigate} from "react-router-dom";

const TextPost = (props) => {

  const navigate = useNavigate();

  const clickHandler = (e) => {
    navigate(`/postreview/${props.id}`)
  }

  return (
    <div className="text-only" onClick={clickHandler} >
      <div className="overlap-group-wrapper">
        <div className="overlap-group">
          <div className="text-wrapper">By {props.owner}</div>
          <div className="div">{props.description}</div>
          <div className="text-wrapper-2">{props.title}</div>
        </div>
      </div>
    </div>
  );
};

export default TextPost;