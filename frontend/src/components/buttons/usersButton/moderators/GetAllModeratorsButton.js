import React from "react";
import "./GetAllModeratorsButton.css"

const GetAllModeratorsButton = ({ onClick }) => {
  return (
    <button className="user-moderator" onClick={onClick}>
      Moderators
    </button>
  );
};

export default GetAllModeratorsButton;