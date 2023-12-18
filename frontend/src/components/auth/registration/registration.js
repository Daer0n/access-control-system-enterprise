import React, { useState } from "react";
import { Link,useNavigate } from 'react-router-dom';
import "./registration.css";
import api from "../../../api/api";


const Registration = () => {
  const [username, setUsername] = useState("Username");
  const [email, setEmail] = useState("Email");
  const [password, setPassword] = useState("Password");
  const [prevUsername, setPrevUsername] = useState("Username");
  const [prevEmail, setPrevEmail] = useState("Email");
  const [prevPassword, setPrevPassword] = useState("Password");
  const [registrationError, setRegistrationError] = useState(false);

  const handleUsernameClick = () => {
    setUsername("");
    setRegistrationError(false);
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
  };

  const handlePasswordBlur = () => {
    if (password === "") {
      setPassword(prevPassword);
    } else {
      setPrevPassword(password);
    }
  };

  const handleEmailClick = () => {
    setEmail("");
  };

  const handleEmailBlur = () => {
    if (email === "") {
      setEmail(prevEmail);
    } else {
      setPrevEmail(email);
    }
  };

  const handleRegistration = async () => {
    try {
      await api.post(`/auth/register/${username}/${email}/${password}`);
    } catch (error) {
      console.error("Registration failed", error);
      alert("Registration failed")
      setRegistrationError(true);
    }
  };

  return (
    <div className="auth-form">
      <div className="block">
        <div className="registration">Registration</div>
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          onClick={handleUsernameClick}
          onBlur={handleUsernameBlur}
          className="input"
        />
        <input
          type="text"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          onClick={handleEmailClick}
          onBlur={handleEmailBlur}
          className="input"
        />
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          onClick={handlePasswordClick}
          onBlur={handlePasswordBlur}
          className="input"
        />
        <button className="submit" onClick={handleRegistration}>
          Submit
        </button>

        <span className="register-bottom">
            <a href="">
            <Link to="/">Login</Link>
            </a>
          </span>
      </div>
    </div>
  );
};

export default Registration;