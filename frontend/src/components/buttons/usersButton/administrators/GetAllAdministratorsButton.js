import React from "react";
import "./GetAllAdministratorsButton.css"

const GetAllAdministratorsButton = ({ onClick }) => {
  return (
    <button className="user-administrator" onClick={onClick}>
      Administrators
    </button>
  );
};

export default GetAllAdministratorsButton;