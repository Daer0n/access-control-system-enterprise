import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./userTables.css";
import api from "../../../api/api";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTimes, faPencilAlt } from "@fortawesome/free-solid-svg-icons";

const UserTable = ({ users, onClick }) => {


    return (
        <div className="container">
            <table className="table table-striped table-bordered table-hover">
                <thead>
                    <th>Id</th>
                    <th>Name</th>
                    <th>Role</th>
                    <th>Email</th>
                    <th>Delete</th>
                </thead>
                <tbody>
                    {users.map((user) => (
                        <tr key={user.id}>
                            <td>{user.id}</td>
                            <td>{user.name}</td>
                            <td>{user.role}</td>
                            <td>{user.email}</td>
                            <td>
                                <button onClick={() => {
                                    onClick(user.id)
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

export default UserTable;
