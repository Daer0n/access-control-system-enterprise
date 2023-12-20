import React, { useEffect, useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./fileTables.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTimes } from "@fortawesome/free-solid-svg-icons";

const FileTable = ({ files, onClick }) => {

    return (
        <div className="container files-table">
            <h1>Files</h1>
            <table className="table table-striped table-bordered table-hover">
                <thead>
                    <tr>
                        <th>Id</th>
                        <th>Name</th>
                        <th>Path</th>
                        <th>Access type</th>
                        <th>Delete</th>
                    </tr>
                </thead>
                <tbody>
                    {files.map((file) => (
                        <tr key={file.id}>
                            <td>{file.id}</td>
                            <td>{file.name}</td>
                            <td>{file.path}</td>
                            <td>{file.access_type}</td>
                            <td>
                                <button
                                    onClick={() => {
                                        onClick(file.id);
                                    }}
                                >
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

export default FileTable;
