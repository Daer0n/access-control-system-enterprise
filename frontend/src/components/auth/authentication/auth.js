import React, { useState } from "react";
import { Link,useNavigate } from 'react-router-dom';
import "./auth.css";
import api from "../../../api/api";
import Registration from "../registration/registration";
import AdministratorMainPage from "../../pages/administratorMainPage/administratorMainPage";

const Login = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState("Username");
  const [password, setPassword] = useState("Password");
  const [prevUsername, setPrevUsername] = useState("Username");
  const [prevPassword, setPrevPassword] = useState("Password");
  const [loginError, setLoginError] = useState(false); 
  const [passwordError, setPasswordError] = useState(false); 

  const handleUsernameClick = () => {
    setUsername("");
    setLoginError(false); 
  };

  const handleUsernameBlur = () => {
    if (username === "") {
      setUsername(prevUsername);
    } else {
      setPrevUsername(username);
    }
  };

  const handlePasswordClick = () => {
    setPassword("");
    setPasswordError(false); 
  };

  const handlePasswordBlur = () => {
    if (password === "") {
      setPassword(prevPassword);
    } else {
      setPrevPassword(password);
    }
  };

  const handleAuth = async () => {
    try {
      await api.post(`/auth/login/${username}/${password}/`);
      navigate("/administrator/main");
    } catch (error) {
      setLoginError(true); 
      setPasswordError(true); 
      console.error("Authentication failed", error);
      alert("Authentication failed")
    }
  };


  return (
    <div className="auth-form">
        <div className="block">
          <div className="login">Login</div>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            onClick={handleUsernameClick}
            onBlur={handleUsernameBlur}
            className={`input ${loginError ? "error" : ""}`}
          />
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            onClick={handlePasswordClick}
            onBlur={handlePasswordBlur}
            className={`input ${passwordError ? "error" : ""}`}
          />
          <button className="submit" onClick={handleAuth}>
            Submit
          </button>

          <span className="register-bottom">
            Don’t have an account?{" "}
            <a href="">
            <Link to="/registration">Register</Link>
            </a>
          </span>
        </div>
    </div>
  );
};

export default Login;