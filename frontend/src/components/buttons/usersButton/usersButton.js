import React from "react";
import "./usersButton.css";

const UsersButton = ({ onClick }) => {
  return (
    <button className="users" onClick={onClick}>
      Users
    </button>
  );
};

export default UsersButton;