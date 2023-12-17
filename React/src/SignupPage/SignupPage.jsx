import React, {useState} from "react";
import "./SignupPageStyle.css";
import {useNavigate} from "react-router-dom";

const SignupPage = () => {

    const options = [
      {label: "Student", value: "Student"},
      {label: "Staff", value: "Staff"},
      {label: "Instructor", value: "Instructor"},
    ]

    const [password, set_password] = useState("");
    const [username, set_username] = useState("");
    const [bilkentID, set_bilkentID] = useState("");
    const [usertype, set_usertype] = useState("Student");
    const [confirmPassword, set_confirmPass] = useState("");
    const [errMessage_email, set_errMessage_email] = useState("");
    const [errMessage_mismatch, set_errMessage_mismatch] = useState("");
    const [email, set_email] = useState("");
    // const [passwordError,set_passwordError]=useState(false);
    // const [confirmPassError,set_confirmPassError]=useState(false);

    const navigate = useNavigate();

    const emailValid = () => {
      const EmailRegex=/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      if(EmailRegex.test(email)){
        set_errMessage_email("");
      }
      else{
        set_errMessage_email("Email is not valid");
      }
    }

    const clickHandler1 = (event) => {
    event.preventDefault();
      navigate ("/login");
    }

    const clickHandler2 = (event) => {
    event.preventDefault();
    emailValid();
    if(password == ""){
      set_errMessage_mismatch("Please enter a password");
    }
    else if(confirmPassword !== password){
      set_errMessage_mismatch("Passwords do not match");
    }
    else if(errMessage_email.length>0){
      set_errMessage_mismatch("");
    }
    else{
      set_errMessage_mismatch("");
      fetch("http://localhost:5000/register", 
      {
        method: "POST",
        headers: {
          "content-type": "application/json"
        },
        body: JSON.stringify({bilkent_id: bilkentID,
                              username: username,
                              password: password,
                              usertype: usertype,
                              pp: "https://bilkonectbucket.s3.eu-north-1.amazonaws.com/c9462708-0858-4d27-ab10-eb342c7ec8ef.jpg ",
                              email: email})
      }
      )
      .then(response => {response.json()
            navigate("/login")}
      )
      .catch(err=> console.log(err))
    }
        
    
    }

  return (
    <div className="element-signup-page">
      <div className="overlap-group-wrapper">
        <div className="overlap-group"> 
          <div className="overlap">
            <div className="div">

              {/* this is user type */}
            <div>
                <select className="rectangleInput1" onChange = { (e) => set_usertype(e.target.value)}> 
                {options.map(option => (
                  <option value={option.value}>{option.label}</option>
                ))}
                </select>
                
            </div>
            {/* this is bilkentID */}
            <div>
                <input className="rectangleInput2" 
                type = "text"
                value = {bilkentID}
                onChange={(e) => set_bilkentID(e.target.value)}
                />
            </div>

            {/* this is password box */}
            <div>
                <input className="rectangleInput4" 
                type="password" 
                value = {password}
                onChange = {(e) => set_password(e.target.value)}
                />
            </div>
            {/* this is confirm pass */}
            <div>
                <input className="rectangleInput3" 
                type="password" 
                value = {confirmPassword}
                onChange = {(e) => set_confirmPass(e.target.value)}
                />
            </div>

            {/* {confirmPassError? <span className="mismatch">Passwords not matched</span>:null} */}

              <div className="text-wrapper">Username</div>
              <div className="text-wrapper-2">Bilkent ID</div>
              <div className="text-wrapper-3">Confirm password</div>
              <div className="text-wrapper-4">Password</div>
              <div className="text-wrapper-5">User Type</div>

              <div>
                <input className="rectangleInput5" 
                value = {email}
                type="text"
                id = 'mail'
                placeholder = 'example@ug.bilkent.edu.tr'
                onChange = {(e) => set_email(e.target.value)}
                />
            </div>
            <div>
                <input className="rectangleInput6" 
                type="text"
                value = {username}
                onChange = {(e) => set_username(e.target.value)}
                />

            </div>
              <div className="text-wrapper-7">Email address</div>
              <div className="continue-wrapper">
                <div className= "text-wrapper-11"onClick = {clickHandler2}>Continue</div>
                <p
                  className = "error_mismatch"> {errMessage_mismatch}
                </p>
                <p
                  className = "error_email"> {errMessage_email}
                </p>
                </div>

              <img className="img" alt="Image" src="https://c.animaapp.com/clwJRseT/img/image-32@2x.png" />
            </div>
            <div className="text-wrapper-8">Create your account</div>
            <p className="already-have-an">
              <span className="span">Already have an account? </span>
              <span className="text-wrapper-9" onClick={clickHandler1}>Log in</span>
            </p>
          </div>
          <div className="div-wrapper">
            <div className="text-wrapper-10">Bilkonect</div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SignupPage;
