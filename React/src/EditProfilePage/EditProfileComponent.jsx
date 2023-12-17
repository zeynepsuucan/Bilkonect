import React, {useState, useRef}  from "react";
import "./EditProfileComponentStyle.css";

import {useNavigate} from "react-router-dom";

import AWS from "aws-sdk";

 

const EditProfileComponent = (props) => {

     // Create state to store file
  const navigate = useNavigate();
  
  const [file, setFile] = useState(null);
  const inputRef = useRef(null);

  const [image, set_image] = useState("");

  const handleImageClick = () => {
    inputRef.current.click();
  }

  const handleImageUpload = async (event) => {
    // Uploaded file
  const file = event.target.files[0];
  // Changing file state
  setFile(file);

  set_image("https://bilkonectbucket.s3.amazonaws.com/" + file.name +"");

  };

  // Function to upload file to s3
  const uploadFile = async () => {

    // S3 Bucket Name
    const S3_BUCKET = "bilkonectbucket";

    // S3 Region
    const REGION = "eu-north-1";

    // S3 Credentials
    AWS.config.update({
      accessKeyId: "AKIA3B7QGBMNUBWBDQQY",
      secretAccessKey: "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",
    });
    const s3 = new AWS.S3({
      params: { Bucket: S3_BUCKET },
      region: REGION,
    });

    // Files Parameters

    const params = {
      Bucket: S3_BUCKET,
      Key: file.name,
      Body: file,
    };

    // Uploading file to s3

    var upload = s3
      .putObject(params)
      .on("httpUploadProgress", (evt) => {
        // File uploading progress
        console.log(
          "Uploading " + parseInt((evt.loaded * 100) / evt.total) + "%"
        );
      })
      .promise();

    await upload.then((err, data) => {
      console.log(err);
      // Fille successfully uploaded
    
    });
  };
  // Function to handle file and store it to file state

    const [username, set_username] = useState(sessionStorage.getItem("username"));
    const [bilkent_id, set_bilkent_id] = useState("");
  
    const createHandler = (event) => {

      if(image !== "")
        uploadFile();
    
        fetch("http://localhost:5000/register", 
      {
        method: "PUT",
        headers: {
          "content-type": "application/json"
        },
        body: JSON.stringify({
            bilkent_id: bilkent_id,
            username: username,
            pp: image
                            })
      }
      )
      .then(response => {response.json();
        
        if (response.status !== 404){
          sessionStorage.setItem("username", username);
          alert("Profile updated successfully.");
          navigate("/postspage");
        }
        else {
          alert("Please insert your valid Bilkent ID");
        }
      })
        
      .catch(err=> console.log(err));

    };

  return (

    <div className="edit-profile-frame">
      <div className="overlap-group-wrapper">
        <div className="overlap-group">
          
         <div className="overlap-2">
          <div className="div">Add photo: </div>
            <div className="ellipse" />
            <div onClick={handleImageClick}>
              <div className="text-wrapper-5" alt = "">+</div>
              <input  type= "file" ref = {inputRef} onChange= {handleImageUpload} style= {{display: 'none'}} />
            </div>
         </div>

          <input className="rectangle" 
          type="text" 
          value = {bilkent_id}
          placeholder="Enter your Bilkent ID here..."
          onChange = {(e) => set_bilkent_id(e.target.value)}/>

            <input className="rectangle-2" 
          type="text" 
          value = {username}
          placeholder="Enter your new username here..."
          onChange = {(e) => set_username(e.target.value)}/>
          
          <div className="overlap">
            <div className="text-wrapper-2" onClick = {createHandler}>update</div>
          </div>
    
          <div className="text-wrapper-4">Enter your Bilkent ID:</div>
          <div className="text-wrapper-user">Enter your new username:</div>
          <img className="image" alt="Image" src="https://c.animaapp.com/EmWF9VUV/img/image-39@2x.png" />
          
        </div>
      </div>
    </div>
  );
};

export default EditProfileComponent;