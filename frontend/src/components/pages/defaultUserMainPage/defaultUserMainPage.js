import React, { useState } from "react";
import "./defaultUserMainPage.css";
import LogoutButton from "../../buttons/logoutButton/logoutButton";
import FoldersButton from "../../buttons/foldersButton/foldersButton";
import UsersButton from "../../buttons/usersButton/usersButton";
import FolderTable from "../../tables/folderTables/folderTables";

const DefaultUserMainPage = () => {
    const [showAdditionalButtons, setShowAdditionalButtons] = useState(false);
    const [showFoldersTable, setShowFoldersTable] = useState(false);

    const handleFoldersButtonClick = async () => {
        setShowFoldersTable((prevState) => !prevState);
    };

    return (
        <div className="main">
            <nav className="nav-bar">
                <div className="left-buttons">
                    <FoldersButton onClick={handleFoldersButtonClick} />
                </div>
                <LogoutButton className="logout" />
            </nav>

            <div className="main-content">
                <div className="content">
                    {showFoldersTable && <FolderTable />}
                </div>
            </div>
        </div>
    );
};

export default DefaultUserMainPage;
