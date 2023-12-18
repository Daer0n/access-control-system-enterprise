import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./App.css";
import Login from "../auth/authentication/auth";
import Registration from "../auth/registration/registration";
import AdministratorMainPage from "../pages/administratorMainPage/administratorMainPage";

function App() {
    return (
        <div className="app">
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<Login />} />
                    <Route path="/registration" element={<Registration />} />
                    <Route path="/administrator/main" element={<AdministratorMainPage />}/>
                </Routes>
            </BrowserRouter>
        </div>
    );
}

export default App;