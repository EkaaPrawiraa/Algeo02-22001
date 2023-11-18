import UploadDataset from "./UploadDataset";
import React, { useState } from 'react';

const Result = () => {
  const [selectedImages, setSelectedImages] = useState([]);

  const handleImagesSelect = (images) => {
    setSelectedImages(images);
  };

  return (
    <div className="Result">
      <UploadDataset onImagesSelect={handleImagesSelect} />
    </div>
  );
};

export default Result;
