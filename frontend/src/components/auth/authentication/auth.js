import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./auth.css";
import api from "../../../api/api";

const Login = () => {
    const navigate = useNavigate();
    const [username, setUsername] = useState("Username");
    const [password, setPassword] = useState("Password");
    const [loginError, setLoginError] = useState(false);
    const [passwordError, setPasswordError] = useState(false);

    const handleUsernameClick = () => {
        setUsername("");
        setLoginError(false);
    };

    const handleUsernameBlur = () => {
        if (username === "") {
            setUsername("Username");
        }
    };

    const handlePasswordClick = () => {
        setPassword("");
        setPasswordError(false);
    };

    const handlePasswordBlur = () => {
        if (password === "") {
            setPassword("Password");
        }
    };

    const handleAuth = async () => {
        try {
            const response = await api.post(
                `/auth/login/${username}/${password}/`
            );
            const userRole = response.data.role;
            if (userRole === "DefaultUser") {
                navigate("/user/main");
            } else if (userRole === "Moderator") {
                navigate("/moderator/main");
            } else if (userRole === "Administrator") {
                navigate("/administrator/main");
            }
        } catch (error) {
            setLoginError(true);
            setPasswordError(true);
            console.error("Authentication failed", error);
            alert("Authentication failed");
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
                    <Link to="/registration">Register</Link>
                </span>
            </div>
        </div>
    );
};

export default Login;
