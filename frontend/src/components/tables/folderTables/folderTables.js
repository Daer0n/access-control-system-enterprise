import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./folderTables.css"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTimes } from "@fortawesome/free-solid-svg-icons";

const FolderTable = ({ folders, onClick }) => {


    return (
        <div className="container folders-table">
            <table className="table table-striped table-bordered table-hover">
                <thead>
                    <th>Id</th>
                    <th>Name</th>
                    <th>Path</th>
                </thead>
                <tbody>
                    {folders.map((folder) => (
                        <tr key={folder.id}>
                            <td>{folder.id}</td>
                            <td>{folder.name}</td>
                            <td>{folder.path}</td>
                            <td>
                                <button onClick={() => {
                                    onClick(folder.id)
                                }}>
                                    <FontAwesomeIcon icon={faTimes} />
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default FolderTable;
