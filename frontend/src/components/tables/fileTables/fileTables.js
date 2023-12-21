import React, { useEffect, useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./fileTables.css";
import api from "../../../api/api";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTimes } from "@fortawesome/free-solid-svg-icons";
import FileInputForm from "../../inputs/fileInput/fileInput";

const FileTable = ({ folder, files, onClick }) => {
  const [showAddForm, setShowAddForm] = useState(false);

  const showFileInputForm = () => {
    console.log(folder);
    setShowAddForm(true);
  };

  const handleFormSubmit = async (name, path, accessType) => {
    try {
      await api.post(`/file/file/${name}/${path}/${folder.id}/${accessType}/`);
      setShowAddForm(false);
    } catch {
      setShowAddForm(false);
    }
  };


  return (
    <div className="container files-table">
      <h1>Files in the "{folder.name}" folder</h1>
      {!showAddForm && (
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
                  <button onClick={() => onClick(file.id)}>
                    <FontAwesomeIcon icon={faTimes} />
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {showAddForm ? (
        <FileInputForm onSubmit={handleFormSubmit} />
      ) : (
        <button className="add-file" onClick={showFileInputForm}>
          Add File
        </button>
      )}
    </div>
  );
};

export default FileTable;