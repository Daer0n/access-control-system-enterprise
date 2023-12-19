import React from "react";
import "./foldersButton.css";

const FoldersButton = ({ onClick }) => {
    return (
        <button className="folders" onClick={onClick}>
            Folders
        </button>
    );
};

export default FoldersButton;
