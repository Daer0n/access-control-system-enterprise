import React, { useState } from "react";
import { Link,useNavigate } from 'react-router-dom';
import "./logoutButton.css";
import api from "../../../api/api";

const LogoutButton = () => {
    const navigate = useNavigate();

    const handleRegistration = async () => {
        await api.post("/auth/logout/");
        navigate("/");
    };

    return (
        <button className="logout" onClick={handleRegistration}>
            Logout
        </button>
    );
};

export default LogoutButton;
