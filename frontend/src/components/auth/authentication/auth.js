import React, { useState } from "react";
import "./auth.css";
import api from "../../../api/api";
import RegistrationComponent from "../registration/registration";
import AdministratorMainPage from "../../pages/administratorMainPage/administratorMainPage";

const AuthComponent = () => {
  const [username, setUsername] = useState("Username");
  const [password, setPassword] = useState("Password");
  const [prevUsername, setPrevUsername] = useState("Username");
  const [prevPassword, setPrevPassword] = useState("Password");
  const [showRegistration, setShowRegistration] = useState(false);
  const [loggedIn, setLoggedIn] = useState(false);
  const [loginError, setLoginError] = useState(false); // Добавлено состояние ошибки авторизации
  const [passwordError, setPasswordError] = useState(false); // Добавлено состояние ошибки пароля

  const handleUsernameClick = () => {
    setUsername("");
    setLoginError(false); // Сбрасывает состояние ошибки логина при клике на инпут
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
    setPasswordError(false); // Сбрасывает состояние ошибки пароля при клике на инпут
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
      await api.post(`/auth/login/${username}/${password}`);
      setLoggedIn(true);
    } catch (error) {
      console.error("Authentication failed", error);
      setLoginError(true); // Устанавливает ошибку логина
      setPasswordError(true); 
    }
  };

  const handleRegisterClick = () => {
    setShowRegistration(true);
  };

  if (loggedIn) {
    return <AdministratorMainPage />;
  }

  return (
    <div className="auth-form">
      {showRegistration ? (
        <RegistrationComponent />
      ) : (
        <div className="block">
          <div className="login">Login</div>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            onClick={handleUsernameClick}
            onBlur={handleUsernameBlur}
            className={`input ${loginError ? "error" : ""}`} // Добавлено условие для применения класса "error" при ошибке логина
          />
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            onClick={handlePasswordClick}
            onBlur={handlePasswordBlur}
            className={`input ${passwordError ? "error" : ""}`} // Добавлено условие для применения класса "error" при ошибке пароля
          />
          <button className="submit" onClick={handleAuth}>
            Submit
          </button>

          <span className="register-bottom">
            Don’t have an account?{" "}
            <a href="#" onClick={handleRegisterClick}>
              Register
            </a>
          </span>
        </div>
      )}
    </div>
  );
};

export default AuthComponent;