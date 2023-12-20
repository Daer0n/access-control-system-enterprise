import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./App.css";
import Login from "../auth/authentication/auth";
import Registration from "../auth/registration/registration";
import AdministratorMainPage from "../pages/administratorMainPage/administratorMainPage";
import ModeratorMainPage from "../pages/moderatorMainPage/moderatorMainPage";
import DefaultUserMainPage from "../pages/defaultUserMainPage/defaultUserMainPage";


function App() {
    return (
        <div className="app">
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<Login />} />
                    <Route path="/registration" element={<Registration />} />
                    <Route path="/administrator/main" element={<AdministratorMainPage />}/>
                    <Route path="/moderator/main" element={<ModeratorMainPage />}/>
                    <Route path="/user/main" element={<DefaultUserMainPage />}/>
                </Routes>
            </BrowserRouter>
        </div>
    );
}

export default App;