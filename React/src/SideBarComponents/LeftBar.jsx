import React from "react";
import {Navigate, useNavigate} from "react-router-dom";
import "./LeftBarStyle.css";
import createIMG from './image30.png';
import homeIMG from './image 32.png';
import searchIMG from './image 31.png';
import notiIMG from './image 33.png';
import postsIMG from './image 36.png';
import settingsIMG from './image 35.png';
import logIMG from './image 34.png';
import chatsIMG from './bubble-chat.png';

const LeftBar = () => {

  const navigate = useNavigate();

  const createHandler = (event) => {
    event.preventDefault();

    navigate("/createChoosePage");
  
  };

  const logClickHandler = (event) => {
    event.preventDefault();

    sessionStorage.removeItem("username");
    navigate("/");
  }

  const postsClicker = (event) => {
    event.preventDefault();

    navigate("/postspage");
  }

  const searchClickHandler = (event) => {
    event.preventDefault();

    navigate("/searchPage");
  }

  const homeHandler = (event) => {
    event.preventDefault();

    navigate("/postspage");
  }

  const chatClickHandler = (event) => {
    event.preventDefault();

    navigate("/chatsAccess")
  }

  return (
    <div className="left-bar-frame">
      <div className="div">
        <div className="overlap-bil">
          <div className="text-wrapper-bil">Bilkonect</div>
        </div>
        <div className="overlap-group-bar1">
          <div className="text-wrapper-2 " onClick={postsClicker}>posts</div>
          <div className="text-wrapper-3"onClick={createHandler}>create</div>
          <div className="text-wrapper-4">settings</div>
          <div className="text-wrapper-5" onClick={logClickHandler}>log out</div>
          <div className="text-wrapper-6">notifications</div>
          <div className="text-wrapper-7" onClick={searchClickHandler}>search</div>
          <div className="text-wrapper-8" onClick={homeHandler}>home</div>
          <div className="text-wrapper-9" onClick={chatClickHandler}>chats</div>
          <img className="image" alt="Image" src={createIMG} />
          <img className="img" alt="Image" src={searchIMG} />
          <img className="image-2" alt="Image" src={homeIMG} />
          <img className="image-3" alt="Image" src={notiIMG} />
          <img className="image-4" alt="Image" src={logIMG} />
          <img className="image-5" alt="Image" src={settingsIMG} />
          <img className="image-6" alt="Image" src={postsIMG} />
          <img className="image-7" alt="Image" src={chatsIMG} />
        </div>
      </div>
    </div>

  );
};

export default LeftBar;