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

const AdministratorMainPage = () => {
  const [showAdditionalButtons, setShowAdditionalButtons] = useState(false);
  const [users, setUsers] = useState([]);

  const handleUsersButtonClick = () => {
    setShowAdditionalButtons((prevState) => !prevState);
  };

  const fetchDefaultUsers = async (id) => {
    const response = await api.get(`/user/user/${id}`);
    console.log(response.data);
    setUsers(response.data); // Обновляем состояние users с полученными данными
  };

  const additionalButtons = showAdditionalButtons && (
    <div className="additional-buttons">
      <GetAllDefaultUsersButton onClick={() => fetchDefaultUsers(23)} />
      <GetAllModeratorsButton />
      <GetAllAdministratorsButton />
    </div>
  );

  return (
    <div className="main">
      <nav className="nav-bar">
        <div className="left-buttons">
          <UsersButton onClick={handleUsersButtonClick} />
          <FoldersButton />
        </div>
        <LogoutButton className="logout" />
      </nav>

      <div className="main-content">
        <div className="content">
          {additionalButtons}
          {users.length > 0 && <UserTable users={users} />}
        </div>
      </div>
    </div>
  );
};

export default AdministratorMainPage;