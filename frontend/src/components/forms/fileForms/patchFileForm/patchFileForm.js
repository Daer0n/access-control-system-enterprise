import React, { useState } from "react";
import "./patchFileForm.css"

const PatchFileForm = ({ file, onSubmit }) => {
    const [name, setName] = useState(file.name);
    const [accessType, setAccessType] = useState(file.access_type);

    const handleNameChange = (event) => {
        setName(event.target.value);
    };


    const handleAccessTypeChange = (event) => {
        setAccessType(event.target.value);
    };


    const handleSubmit = (event) => {
        event.preventDefault();
        onSubmit(file.id, accessType);
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
                        <option value="READ">READ</option>
                        <option value="WRITE">WRITE</option>
                        <option value="DELETE">DELETE</option>
                    </select>
                </div>

                <button type="submit" className="add-file">
                    Submit
                </button>
            </form>
        </div>
    );
};

export default PatchFileForm;