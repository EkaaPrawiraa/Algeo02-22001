import React, { useState } from 'react';
import axios from 'axios';

const YourParentComponent = () => {
  const handleUpload = async (event) => {
    const files = event.target.files;
    try {
      const formData = new FormData();
      for (let i = 0; i < files.length; i++) {
        formData.append('files', files[i]);
      }

      const response = await axios.post('http://localhost:8000/api/upload/folder/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      console.log('Files uploaded successfully:', response.data);
      // Handle response if needed
    } catch (error) {
      console.error('Error uploading files:', error);
      // Handle errors if needed
    }
  };

  return (
    <div className='InsertDatasetButton' onClick={() => document.getElementById('ctrl').click()}>
      <input
        hidden
        multiple
        type="file"
        id="ctrl"
        webkitdirectory=""
        directory=""
        accept="image/*"
        onChange={handleUpload}
      />
      <span className="data-button">
        Insert Dataset
      </span>
    </div>
  );
};

export default YourParentComponent;