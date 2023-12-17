import React, { useState } from "react";
import "./auth.css";
import api from "../../../api/api";

const AuthComponent = () => {
    const [username, setUsername] = useState("Username");
    const [password, setPassword] = useState("Password");
    const [prevUsername, setPrevUsername] = useState("Username");
    const [prevPassword, setPrevPassword] = useState("Password");

    const handleUsernameClick = () => {
        setUsername("");
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

    const handleAuth = async () => {
        await api.post(`/auth/login/${username}/${password}`);
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
                    className="input"
                />
                <input
                    type="text"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    onClick={handlePasswordClick}
                    onBlur={handlePasswordBlur}
                    className="input"
                />
                <button className="submit" onClick={handleAuth}>
                    Submit
                </button>

                <span className="register-bottom">
                    Don’t have an account? <a href="#">Register</a>
                </span>
            </div>
        </div>
    );
};

export default AuthComponent;
