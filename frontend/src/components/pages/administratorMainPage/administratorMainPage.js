import React, { useState } from "react";
import "./administratorMainPage.css";
import api from "../../../api/api";
import LogoutButton from "../../buttons/logoutButton/logoutButton";
import FoldersButton from "../../buttons/foldersButton/foldersButton";
import UsersButton from "../../buttons/usersButton/usersButton";
import GetAllDefaultUsersButton from "../../buttons/usersButton/users/GetAllDefaultUsersButton";
import UserTable from "../../tables/userTables/userTables";
import GetAllModeratorsButton from "../../buttons/usersButton/moderators/GetAllModeratorsButton";
import GetAllAdministratorsButton from "../../buttons/usersButton/administrators/GetAllAdministratorsButton";
import FolderTable from "../../tables/folderTables/folderTables";

const AdministratorMainPage = () => {
    const [showAdditionalButtons, setShowAdditionalButtons] = useState(false);
    const [defaultUsers, setDefaultUsers] = useState([]);

    const [administrators, setAdministrators] = useState([]);
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

    const handleShowAdministratorsTable = async () => {
        await fetchAdministrators();
        setShowAdministratorsTable((prevState) => !prevState);
        setShowDefaultUsersTable(false);
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

    const handleDeleteAdministratorsClick = async (id) => {
        try {
            await api.delete(`/user/administrator/${id}`);
            await fetchAdministrators();
        } catch (error) {
            console.error("Failed to delete administrator", error);
            alert("Failed to delete administrator");
        }
    };

    const handleDeleteModeratorsClick = async (id) => {
        try {
            await api.delete(`/user/moderator/${id}`);
            await fetchAdministrators();
        } catch (error) {
            console.error("Failed to delete moderator", error);
            alert("Failed to delete moderator");
        }
    };

    const fetchDefaultUsers = async () => {
        try {
            const response = await api.get("/user/users/");
            setDefaultUsers(response.data);
        } catch(error) {
            console.error("Failed to fetch users", error);
        }
    };

    const fetchAdministrators = async () => {
        try {
            const response = await api.get("/user/administrators/");
            setAdministrators(response.data);
        } catch (error) {
            console.error("Failed to fetch administrators", error);
        }
    };

    const fetchModerators = async () => {
        try {
            const response = await api.get("/user/moderators/");
            setModerators(response.data);
        } catch(error) {
            console.error("Failed to fetch moderators", error);
        }
    };

    const additionalButtons = showAdditionalButtons && (
        <div className="additional-buttons">
            <GetAllDefaultUsersButton onClick={handleShowDefaultUsersTable} />
            <GetAllModeratorsButton onClick={handleShowModeratorsTable} />
            <GetAllAdministratorsButton
                onClick={handleShowAdministratorsTable}
            />
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
                    {showAdministratorsTable && (
                        <UserTable
                            users={administrators}
                            onClick={handleDeleteAdministratorsClick}
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

export default AdministratorMainPage;
