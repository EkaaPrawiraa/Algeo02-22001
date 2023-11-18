const UploadDataset = ({ onImagesSelect }) => {
  const handleFileChange = (event) => {
    const files = event.target.files;
    if (files.length > 0) {
      onImagesSelect(Array.from(files));
    }
  };

  return (
    <div className="DatasetButton">
        <label for="Dataset">
            <p>
                Upload Dataset
            </p>
        </label>
      <input type="file" id='Dataset' multiple onChange={handleFileChange} />
    </div>
  );
};

export default UploadDataset;
