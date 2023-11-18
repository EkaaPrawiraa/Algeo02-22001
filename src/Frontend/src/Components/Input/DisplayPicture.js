import React from 'react';

const DisplayPicture = ({ imageData }) => {
  return (
    <div className="InputPicture">
      <img src={imageData} alt="Selected" style={{ maxWidth: '100%', maxHeight: '400px' }} />
    </div>
  );
};

export default DisplayPicture;