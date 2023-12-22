import React, { useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./folderTables.css";
import api from "../../../api/api";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTimes, faPlus } from "@fortawesome/free-solid-svg-icons";
import FileTable from "../fileTables/fileTables";
import AddFolderForm from "../../forms/folderForms/addFolderForm";

const FolderTable = () => {
  const [folders, setFolders] = useState([]);
  const [files, setFiles] = useState([]);
  const [folder, setFolder] = useState(null);
  const [showFiles, setShowFiles] = useState(false);
  const [showAddFolderForm, setShowAddFolderForm] = useState(false);
  const [showTable, setShowTable] = useState(true);
  const [showAddButton, setShowAddButton] = useState(true);

  useEffect(() => {
    fetchFolders();
  }, []);

  const fetchFolders = async () => {
    try {
      const response = await api.get("/file/folders/");
      setFolders(response.data);
    } catch (error) {
      console.error("Failed to fetch folders", error);
    }
  };

  const handleShowFiles = async (selectedFolder) => {
    setFolder(selectedFolder);
    setShowFiles(true);
    await fetchFiles(selectedFolder.id);
    setShowTable(false);
    setShowAddButton(false);
    setShowAddFolderForm(false);
  };

  const handleDeleteFoldersClick = async (id) => {
    try {
      await api.delete(`/file/folder/${id}`);
      await fetchFolders();
    } catch (error) {
      console.error("Failed to delete folders", error);
      alert("Failed to delete folders");
    }
  };

  const fetchFiles = async (folder_id) => {
    try {
      const response = await api.get(`/file/folder/${folder_id}/files`);
      setFiles(response.data);
    } catch (error) {
      console.error("Failed to fetch files", error);
    }
  };

  const handleDeleteFile = async (id) => {
    try {
      console.log(id);
      await api.delete(`/file/file/${id}/`);
      await fetchFiles(folder.id);
    } catch (error) {
      console.error("Failed to delete file", error);
      alert("Failed to delete file");
    }
  };

  const handleFormSubmit = async (name, path) => {
    try {
      await api.post(`file/folder/${name}/${path}/`);
      await fetchFolders();
      setShowAddFolderForm(false);
      setShowTable(true);
    } catch (error) {
      console.error("Failed to add folder", error);
      alert("Failed to add folder");
    }
  };

  const handleAddFolder = () => {
    setShowAddFolderForm(!showAddFolderForm);
    setShowTable(false);
    setShowAddButton(false);
    setShowFiles(false);
  };

  return (
    <div className="container folders-table">
      {showTable && (
        <table className="table table-striped table-bordered table-hover">
          <thead>
            <tr>
              <th>Name</th>
              <th>Path</th>
              <th>Files</th>
              <th>Delete</th>
            </tr>
          </thead>
          <tbody>
            {folders.map((folder) => (
              <tr key={folder.id}>
                <td>{folder.name}</td>
                <td>{folder.path}</td>
                <td>
                  <button onClick={() => handleShowFiles(folder)}>
                    <FontAwesomeIcon icon={faPlus} />
                  </button>
                </td>
                <td>
                  <button
                    onClick={() => handleDeleteFoldersClick(folder.id)}
                  >
                    <FontAwesomeIcon icon={faTimes} />
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {showAddButton && (
        <button className="add-folder" onClick={handleAddFolder}>
          Add folder
        </button>
      )}

      {showAddFolderForm && (
        <AddFolderForm onSubmit={handleFormSubmit} />
      )}

      {showFiles && folder && (
        <FileTable folder={folder} files={files} onClick={handleDeleteFile} />
      )}
    </div>
  );
};

export default FolderTable;