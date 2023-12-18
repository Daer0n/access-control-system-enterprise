import React from "react";
import "./GetAllDefaultUsersButton.css"

const GetAllDefaultUsersButton = ({ onClick }) => {
  return (
    <button className="user-default" onClick={onClick}>
      Default users
    </button>
  );
};

export default GetAllDefaultUsersButton;