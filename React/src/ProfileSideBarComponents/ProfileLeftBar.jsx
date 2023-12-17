import React from "react";
import "./ProfileLeftBarStyle.css";
import blockedIMG from './image 37.png';
import archivedIMG from './archive (1) 2.png';
import requestIMG from './add-user 2.png';
import notiIMG from './image 33.png';
import favIMG from './image 36.png';
import settingsIMG from './image 35.png';
import logIMG from './image 34.png';
import reportIMG from './image 38.png';

const ProfileLeftBar = () => {
  return (
    <div className="profile-left-bar-frame">
      <div className="div">
        <div className="overlap">
          <div className="text-wrapper">Bilkonect</div>
        </div>
        <div className="overlap-group">
          <div className="text-wrapper-2">favorite posts</div>
          <div className="text-wrapper-3">blocked profiles</div>
          <div className="text-wrapper-4">reports</div>
          <div className="text-wrapper-5">settings</div>
          <div className="text-wrapper-9">log out</div>
          <div className="text-wrapper-6">notifications</div>
          <div className="text-wrapper-7">requests</div>
          <div className="text-wrapper-8">archived posts</div>
          <img className="image" alt="Image" src={blockedIMG} />
          <img className="img" alt="Image" src={requestIMG} />
          <img className="image-2" alt="Image" src={archivedIMG} />
          <img className="image-3" alt="Image" src={notiIMG} />
          <img className="image-4" alt="Image" src={logIMG} />
          <img className="image-5" alt="Image" src={settingsIMG} />
          <img className="image-6" alt="Image" src={favIMG} />
          <img className="image-7" alt= "Image" src= {reportIMG}/> 
        </div>
      </div>
    </div>

  );
};

export default ProfileLeftBar;