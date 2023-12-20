import React, { useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./folderTables.css";
import api from "../../../api/api";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTimes, faPlus } from "@fortawesome/free-solid-svg-icons";
import FileTable from "../fileTables/fileTables";
import AddFolderInput from "../../inputs/folderInput/folderInput";

const FolderTable = () => {
    const [folders, setFolders] = useState([]);
    const [files, setFiles] = useState([]);
    const [showFiles, setShowFiles] = useState(false);
    const [selectedFolderId, setSelectedFolderId] = useState(null);
    const [showAddFolderForm, setShowAddFolderForm] = useState(false);

    useEffect(() => {
        fetchFolders();
    }, []);

    const fetchFolders = async () => {
        try {
            const response = await api.get("/file/folders/");
            setFolders(response.data);
        } catch (error) {
            console.error("Failed to fetch folders", error);
            alert("Failed to fetch folders");
        }
    };

    const handleShowFiles = async (folderId) => {
        setSelectedFolderId(folderId);
        setShowFiles(true);
        await fetchFiles(folderId);
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
            alert("Failed to fetch files");
        }
    };

    const handleDeleteFile = async (id) => {
        try {
            console.log(id);
            await api.delete(`/file/file/${id}/`);
            await fetchFiles(selectedFolderId);
        } catch (error) {
            console.error("Failed to delete file", error);
            alert("Failed to delete file");
        }
    };

    const handleFormSubmit = async (name, path) => {
        try {
            await api.post(`file/folder/${name}/${path}/`);
            // Обновление списка папок после успешного добавления
            await fetchFolders();
        } catch (error) {
            console.error("Failed to add folder", error);
            alert("Failed to add folder");
        }
    };

    const handleAddFolder = () => {
        setShowAddFolderForm(!showAddFolderForm);
    };

    return (
        <div className="container folders-table">
            <h1>Folders</h1>
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
                                <button
                                    onClick={() => handleShowFiles(folder.id)}
                                >
                                    <FontAwesomeIcon icon={faPlus} />
                                </button>
                            </td>
                            <td>
                                <button onClick={() => handleDeleteFoldersClick(folder.id)}>
                                    <FontAwesomeIcon icon={faTimes} />
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>

            {showAddFolderForm ? (
                <AddFolderInput onSubmit={handleFormSubmit} />
            ) : (
                <button className="add-folder" onClick={handleAddFolder}>
                    Add folder
                </button>
            )}

            {showFiles && <FileTable files={files} onClick={handleDeleteFile} />}
        </div>
    );
};

export default FolderTable;