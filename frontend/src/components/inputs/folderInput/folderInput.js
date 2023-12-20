import React, { useState } from "react";

const AddFolderInput = ({ onSubmit }) => {
    const [name, setName] = useState("");
    const [path, setPath] = useState("");

    const handleNameChange = (event) => {
        setName(event.target.value);
    };

    const handlePathChange = (event) => {
        setPath(event.target.value);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        onSubmit(name, path);
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

                <button type="submit" className="add-folder">
                    Submit
                </button>
            </form>
        </div>
    );
};

export default AddFolderInput;