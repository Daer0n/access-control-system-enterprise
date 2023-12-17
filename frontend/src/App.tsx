import React from "react";
import "./App.css";
import AuthComponent from "./components/auth/authentication/auth";
import RegistrationComponent from "./components/auth/registration/registration";

function App() {
    return (
        <div className="app">
            <AuthComponent />
        </div>
    );
}

export default App;
