import React, { useState } from "react";
import "./registration.css";
import api from "../../../api/api";

const RegistrationComponent = () => {
    const [username, setUsername] = useState("Username");
    const [email, setEmail] = useState("Email");
    const [password, setPassword] = useState("Password");
    const [prevUsername, setPrevUsername] = useState("Username");
    const [prevEmail, setPrevEmail] = useState("Email");
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

    const handleAuth = async () => {
        await api.post(`/auth/register/${username}/${email}/${password}`);
    };

    return (
        <div className="auth-form">
            <div className="block">
                <div className="login">Registration</div>
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
            </div>
        </div>
    );
};

export default RegistrationComponent;
