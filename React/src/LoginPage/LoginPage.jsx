import React, {useState} from "react";
import "./LoginPageStyle.css";
import {useNavigate} from "react-router-dom";

const LoginPage = () => {

  const [userInfo, set_userInfo] = useState("");
  const [password, set_password] = useState("");
  const [errMessage_mismatch, set_errMessage_mismatch] = useState("");

  const navigate = useNavigate();

  const clickHandler1 = (event) => {
    event.preventDefault();
    // alert("Hello!");
    navigate("/signup");
  }

  const clickHandler2 = (event) => {
    event.preventDefault();
    if(password == ""){
      set_errMessage_mismatch("Please enter a password");
    }
    else {
      

        fetch("http://localhost:5000/login", 
      {
        method: "POST",
        headers: {
          "content-type": "application/json"
        },
        body: JSON.stringify({
            username: userInfo,
            password: password,
                            })
      }
      )
      .then(response => {response.json();
        
        if (response.status !== 401){
          sessionStorage.setItem("username", userInfo);
          navigate("/postspage");
        }
        else {
          set_errMessage_mismatch("Login failed, try again");
        }
      })
      .catch(err=> console.log(err))
      
    }
  }  
    
    const clickHandler3 = (event) => {
      event.preventDefault();
      // alert("Hello!");
      navigate("/accrecovery");
    }

  return (
    <div className="element-login-page">
      <div className="overlap-group-wrapper">
        <div className="overlap-group">
          <div className="overlap">
            <div className="div">
              <div className="overlap-2">
                <div className="overlap-3">
                  <div>
                    <input className="rectangleInput" 
                    type="text" 
                    value = {userInfo}
                    onChange={(e) => set_userInfo(e.target.value)}
                    />
                  </div>
                  <p className="text-wrapper">username / email / bilkent id</p>
                </div>
                <img className="image" alt="Image" src="https://c.animaapp.com/65dKJiIt/img/image-32@2x.png" />
              </div>
              <div>
              <input className="rectangle-2Input" 
              type="password"
              value = {password}
              onChange={(e) => set_password(e.target.value)}
              />
              </div>
              <div className="text-wrapper-2">password</div>
              <div className="text-wrapper-3"onClick = {clickHandler3}>forgot password?</div>
              <div className="login-wrapper">
              <div className="text-wrapper-7" onClick={clickHandler2}>Login</div>
              </div>
              <p
                  className = "error_mismatch"> {errMessage_mismatch}
              </p>
            </div>
            <div className="text-wrapper-4">Welcome back !</div>
            <p className="don-t-have-an">
              <span className="span">Don’t have an account? </span>
              <span className="text-wrapper-5"onClick={clickHandler1}>Sign up</span>
            </p>
          </div>
          <div className="div-wrapper">
            <div className="text-wrapper-6">Bilkonect</div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
