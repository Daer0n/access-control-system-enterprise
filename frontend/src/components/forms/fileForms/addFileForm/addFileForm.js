import React, { useState } from "react";
import "./addFileForm.css"

const AddFileForm = ({ onSubmit }) => {
    const [name, setName] = useState("");
    const [path, setPath] = useState("");
    const [accessType, setAccessType] = useState("READ");
    const [file, setFile] = useState(null);

    const handleNameChange = (event) => {
        setName(event.target.value);
    };

    const handlePathChange = (event) => {
        setPath(event.target.value);
    };

    const handleAccessTypeChange = (event) => {
        setAccessType(event.target.value);
    };

    const handleFileChange = (event) => {
        const selectedFile = event.target.files[0];
        setFile(selectedFile);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        onSubmit(name, path, accessType, file);
    };

    return (
        <div className="container">
            <form onSubmit={handleSubmit}>
                <div className="mb-3 mt-3">
                    <label htmlFor="name" className="form-label">
                        Name
                    </label>
                    <input
                        type="text"
                        className="form-control"
                        id="name"
                        name="name"
                        onChange={handleNameChange}
                        value={name}
                    />
                </div>

                <div className="mb-3">
                    <label htmlFor="path" className="form-label">
                        Path
                    </label>
                    <input
                        type="text"
                        className="form-control"
                        id="path"
                        name="path"
                        onChange={handlePathChange}
                        value={path}
                    />
                </div>

                <div className="mb-3">
                    <label htmlFor="access_type" className="form-label">
                        Access type
                    </label>
                    <select
                        className="form-control"
                        id="access_type"
                        name="access_type"
                        value={accessType}
                        onChange={handleAccessTypeChange}
                    >
                        <option value="Read">READ</option>
                        <option value="Write">WRITE</option>
                        <option value="Delete">DELETE</option>
                    </select>
                </div>

                <div className="mb-3">
                    <label htmlFor="file" className="form-label">
                        File
                    </label>
                    <input
                        type="file"
                        className="form-control"
                        id="file"
                        name="file"
                        onChange={handleFileChange}
                    />
                </div>

                <button type="submit" className="add-file">
                    Submit
                </button>
            </form>
        </div>
    );
};

export default AddFileForm;