import React, { useState } from 'react';
import axios from 'axios';

// FolderUploadButton
const FolderUploadButton = ({ onFolderSelect, onFolderUpload }) => {
  const handleSelect = (event) => {
    const folder = event.target.files[0];
    onFolderSelect(folder);
  };

  const handleUpload = () => {
    onFolderUpload();
  };

  return (
    <div>
      <input type="file" id="folderInput" webkitdirectory="" directory="" onChange={handleSelect} />
      <button onClick={handleUpload}>Upload Folder</button>
    </div>
  );
};

// YourParentComponent
const YourParentComponent = () => {
  const [selectedFolder, setSelectedFolder] = useState(null);

  const handleFolderSelect = (folder) => {
    setSelectedFolder(folder);
  };

  const handleFolderUpload = async () => {
    try {
      const formData = new FormData();
      formData.append('file', selectedFolder);

      // Kirim request ke backend Anda
      const response = await axios.post('http://localhost:8000/api/upload/folder/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      // Handle respons jika diperlukan
      console.log('Upload berhasil', response.data);
    } catch (error) {
      // Handle error
      console.error('Error mengupload folder', error.response.data);
    }
  };

  return (
    <div>
      <FolderUploadButton onFolderSelect={handleFolderSelect} onFolderUpload={handleFolderUpload} />
    </div>
  );
};

export default YourParentComponent;
