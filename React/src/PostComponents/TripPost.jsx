import React from "react";
import "./TripPostStyle.css";
import {useNavigate} from "react-router-dom";

const TripPost = (props) => {

  const navigate = useNavigate();

  const clickHandler = (e) => {
    navigate(`/postreview/${props.id}`)
  }
  
  return (
    <div className="trip-frame" onClick={clickHandler} >
      <div className="overlap-group-wrapper">
        <div className="overlap-group">
          <div className="text-wrapper">By {props.owner} </div>
          <div className="div">{props.description} </div>
          <div className="text-wrapper-2">{props.title} </div>
          <div className="trip-info-wrapper">From: {props.departure} <br/> To: {props.destination} <br/> When:   <br/> {props.tripDate} </div>
        </div>
      </div>
    </div>
  );
};

export default TripPost;