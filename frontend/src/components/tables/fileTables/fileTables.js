import React, { useEffect, useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./fileTables.css";
import api from "../../../api/api";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPencilAlt, faTimes } from "@fortawesome/free-solid-svg-icons";
import FileInputForm from "../../forms/fileForms/addFileForm/addFileForm";
import PatchFileForm from "../../forms/fileForms/patchFileForm/patchFileForm";

const FileTable = ({ folder, onClick }) => {
  const [showAddForm, setShowAddForm] = useState(false);
  const [showPatchForm, setShowPatchForm] = useState(false);
  const [selectedFile, setSelectedFile] = useState(null);
  const [files, setFiles] = useState([]);

  useEffect(() => {
    fetchFiles();
  }, []);

  const fetchFiles = async () => {
    try {
      const response = await api.get(`/file/folder/${folder.id}/files`);
      setFiles(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  const showFileInputForm = () => {
    setShowAddForm(true);
  };

  const showPatchFileForm = (file) => {
    setSelectedFile(file);
    setShowPatchForm(true);
  };

  const handleFormSubmit = async (name, path, accessType) => {
    try {
      console.log(folder.id)
      console.log(name)
      console.log(path)
      console.log(accessType)
      await api.post(`/file/file/${name}/${path}/${folder.id}/${accessType}/`);
      setShowAddForm(false);
      fetchFiles(); 
    } catch {
      setShowAddForm(false);
    }
  };

  const handlePatchSubmit = async (fileId, accessType) => {
    try {
      await api.patch(`/file/user/${fileId}/${accessType}/`);
      setShowPatchForm(false);
      fetchFiles();
    } catch {
      setShowPatchForm(false);
    }
  };

  const handleDelete = async (fileId) => {
    try {
      await api.delete(`/file/file/${fileId}`);
      fetchFiles();
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="container files-table">
      <h1>Files in the "{folder.name}" folder</h1>
      {!showAddForm && !showPatchForm && (
        <table className="table table-striped table-bordered table-hover">
          <thead>
            <tr>
              <th>Name</th>
              <th>Path</th>
              <th>Access type</th>
              <th>Modified</th>
              <th>Delete</th>
            </tr>
          </thead>
          <tbody>
            {files.map((file) => (
              <tr key={file.id}>
                <td>{file.name}</td>
                <td>{file.path}</td>
                <td>{file.access_type}</td>
                <td>
                  <button onClick={() => showPatchFileForm(file)}>
                    <FontAwesomeIcon icon={faPencilAlt} />
                  </button>
                </td>
                <td>
                  <button onClick={() => handleDelete(file.id)}>
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
      ) : showPatchForm ? (
        <PatchFileForm file={selectedFile} onSubmit={handlePatchSubmit} />
      ) : (
        <button className="add-file" onClick={showFileInputForm}>
          Add File
        </button>
      )}
    </div>
  );
};

export default FileTable;