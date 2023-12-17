import React, {useState, useRef}  from "react";
import "./IMGCreateStyle.css";
import ReactDom from "react-dom";
import ReactS3 from "react-s3";
import {useNavigate} from "react-router-dom";

import AWS from "aws-sdk";

 

const IMGCreate = (props) => {

     // Create state to store file
  const navigate = useNavigate();
  
  const [file, setFile] = useState(null);
  const inputRef = useRef(null);

  const [image, set_image] = useState("https://bilkonectbucket.s3.eu-north-1.amazonaws.com/c9462708-0858-4d27-ab10-eb342c7ec8ef.jpg ");

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
      alert("File uploaded successfully.");
    });
  };
  // Function to handle file and store it to file state

    const today = new Date();

    const [title, set_title] = useState("");
    const [description, set_description] = useState("");

    const createHandler = (event) => {

      if(image !== "https://bilkonectbucket.s3.eu-north-1.amazonaws.com/c9462708-0858-4d27-ab10-eb342c7ec8ef.jpg ")
        uploadFile();
      

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
            owner: sessionStorage.getItem("username") ,
            criteria: "Good condition",
            share_date: "2023-12-31T12:00:00",
            image: image,
                            })
      }
      )
      .then(response => response.json())
      .catch(err=> console.log(err))
      
      navigate("/postspage");
    };

  return (

    <div className="IMG-create">
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
          value = {title}
          placeholder="Enter your title here..."
          onChange = {(e) => set_title(e.target.value)}/>
          
          <div className="overlap">
            <div className="text-wrapper-2" onClick = {createHandler}>create post</div>
          </div>
          <div className="text-wrapper-3">Add a description:</div>
          <textarea className="rectangle-2" 
            type="text" 
            placeholder="Enter your description here..."
            padding = "10px"
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

export default IMGCreate;