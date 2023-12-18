import React from "react";
import "./administratorMainPage.css";
import LogoutButton from "../../buttons/logoutButton/logoutButton";
import FoldersButton from "../../buttons/foldersButton/foldersButton";
import UsersButton from "../../buttons/usersButton/usersButton";

const AdministratorMainPage = () => {
    return (
        <div className="main">
            <nav className="nav-bar">
                <div className="left-buttons">
                    <UsersButton className="users" />
                    <FoldersButton className="folders" />
                </div>
                <LogoutButton className="logout" />
            </nav>

            <div className="main-content">
                <div className="content">
                    <h1>Hello, World!</h1>
                </div>
            </div>
        </div>
    );
};

export default AdministratorMainPage;
