import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./folderTables.css";
import api from "../../../api/api";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTimes, faPlus } from "@fortawesome/free-solid-svg-icons";
import FileTable from "../fileTables/fileTables";

const FolderTable = ({ folders, onClick }) => {
  const [files, setFiles] = useState([]);
  const [showFiles, setShowFiles] = useState(false);
  const [selectedFolderId, setSelectedFolderId] = useState(null);

  const handleShowFiles = async (folderId) => {
    setSelectedFolderId(folderId);
    setShowFiles(true);
    await fetchFiles(folderId);
  };

  const fetchFiles = async (folder_id) => {
    try {
      const response = await api.get(`/file/folder/${folder_id}/files`);
      setFiles(response.data);
    } catch (error) {
      console.error("Failed to fetch files", error);
      alert("Failed to fetch files");
    }
  };

  const handleDeleteFile = async (id) => {
    try {
      await api.delete(`/file/file/${id}`);
      await fetchFiles(selectedFolderId);
    } catch (error) {
      console.error("Failed to delete file", error);
      alert("Failed to delete file");
    }
  };

  return (
    <div className="container folders-table">
      <table className="table table-striped table-bordered table-hover">
        <thead>
          <tr>
            <th>Id</th>
            <th>Name</th>
            <th>Path</th>
            <th>Files</th>
            <th>Delete</th>
          </tr>
        </thead>
        <tbody>
          {folders.map((folder) => (
            <tr key={folder.id}>
              <td>{folder.id}</td>
              <td>{folder.name}</td>
              <td>{folder.path}</td>
              <td>
                <button onClick={() => handleShowFiles(folder.id)}>
                  <FontAwesomeIcon icon={faPlus} />
                </button>
              </td>
              <td>
                <button onClick={() => onClick(folder.id)}>
                  <FontAwesomeIcon icon={faTimes} />
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      {showFiles && <FileTable files={files} onClick={handleDeleteFile} />}
    </div>
  );
};

export default FolderTable;