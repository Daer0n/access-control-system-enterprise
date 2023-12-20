import React, { useState } from "react";
import "./moderatorMainPage.css";
import api from "../../../api/api";
import LogoutButton from "../../buttons/logoutButton/logoutButton";
import FoldersButton from "../../buttons/foldersButton/foldersButton";
import UsersButton from "../../buttons/usersButton/usersButton";
import GetAllDefaultUsersButton from "../../buttons/usersButton/users/GetAllDefaultUsersButton";
import UserTable from "../../tables/userTables/userTables";
import GetAllModeratorsButton from "../../buttons/usersButton/moderators/GetAllModeratorsButton";
import FolderTable from "../../tables/folderTables/folderTables";

const ModeratorMainPage = () => {
    const [showAdditionalButtons, setShowAdditionalButtons] = useState(false);
    const [defaultUsers, setDefaultUsers] = useState([]);

    const [moderators, setModerators] = useState([]);
    const [showDefaultUsersTable, setShowDefaultUsersTable] = useState(false);
    const [showAdministratorsTable, setShowAdministratorsTable] =
        useState(false);
    const [showModeratorsTable, setShowModeratorsTable] = useState(false);
    const [showFoldersTable, setShowFoldersTable] = useState(false);

    const handleUsersButtonClick = () => {
        setShowAdditionalButtons((prevState) => !prevState);
        setShowAdministratorsTable(false);
        setShowModeratorsTable(false);
        setShowDefaultUsersTable(false);
        setShowFoldersTable(false);
    };

    const handleFoldersButtonClick = async () => {
        setShowFoldersTable((prevState) => !prevState);
        setShowAdditionalButtons(false);
        setShowDefaultUsersTable(false);
        setShowAdministratorsTable(false);
        setShowModeratorsTable(false);
    };

    const handleShowDefaultUsersTable = async () => {
        await fetchDefaultUsers();
        setShowDefaultUsersTable((prevState) => !prevState);
        setShowAdministratorsTable(false);
        setShowModeratorsTable(false);
        setShowFoldersTable(false);
    };


    const handleShowModeratorsTable = async () => {
        await fetchModerators();
        setShowModeratorsTable((prevState) => !prevState);
        setShowAdministratorsTable(false);
        setShowDefaultUsersTable(false);
        setShowFoldersTable(false);
    };

    const handleDeleteDefaultusersClick = async (id) => {
        try {
            await api.delete(`/user/user/${id}`);
            await fetchDefaultUsers();
        } catch (error) {
            console.error("Failed to delete user", error);
            alert("Failed to delete user");
        }
    };

    const handleDeleteModeratorsClick = async (id) => {
        try {
            await api.delete(`/user/moderator/${id}`);
        } catch (error) {
            console.error("Failed to delete moderator", error);
            alert("Failed to delete moderator");
        }
    };

    const fetchDefaultUsers = async () => {
        const response = await api.get("/user/users/");
        setDefaultUsers(response.data);
    };

    const fetchModerators = async () => {
        const response = await api.get("/user/moderators/");
        setModerators(response.data);
    };

    const additionalButtons = showAdditionalButtons && (
        <div className="additional-buttons">
            <GetAllDefaultUsersButton onClick={handleShowDefaultUsersTable} />
            <GetAllModeratorsButton onClick={handleShowModeratorsTable} />
        </div>
    );

    return (
        <div className="main">
            <nav className="nav-bar">
                <div className="left-buttons">
                    <UsersButton onClick={handleUsersButtonClick} />
                    <FoldersButton onClick={handleFoldersButtonClick} />
                </div>
                <LogoutButton className="logout" />
            </nav>

            <div className="main-content">
                <div className="content">
                    {additionalButtons}
                    {showDefaultUsersTable && (
                        <UserTable
                            users={defaultUsers}
                            onClick={handleDeleteDefaultusersClick}
                        />
                    )}
                    {showModeratorsTable && (
                        <UserTable
                            users={moderators}
                            onClick={handleDeleteModeratorsClick}
                        />
                    )}
                    {showFoldersTable && <FolderTable />}
                </div>
            </div>
        </div>
    );
};

export default ModeratorMainPage;
