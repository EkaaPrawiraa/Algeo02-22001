import React, { useState } from 'react';
import axios from 'axios';
const { ipcRenderer } = window.require('electron');

function App() {
  const [selectedFolder, setSelectedFolder] = useState('');

  const openFolderDialog = () => {
    ipcRenderer.send('select-folder');
  };

  ipcRenderer.on('selected-folder', (event, folderPath) => {
    setSelectedFolder(folderPath);
  });

  const uploadFolder = () => {
    if (selectedFolder) {
      const formData = new FormData();
      formData.append('folder', selectedFolder);

      axios.post('http://127.0.0.1:8000/api/upload/folder/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
      .then(response => {
        console.log(response.data);
        // Handle the server response as needed
      })
      .catch(error => {
        console.error('Error uploading folder:', error);
      });
    } else {
      console.error('No folder selected');
    }
  };

  return (
    <div>
      <button onClick={openFolderDialog}>Select Folder</button>
      <p>Selected Folder: {selectedFolder}</p>
      <button onClick={uploadFolder}>Upload Folder</button>
    </div>
  );
}

export default App;
