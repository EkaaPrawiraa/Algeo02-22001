const InputPicture = ({ onImageSelect }) => {
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        const imageData = reader.result;
        onImageSelect(imageData);
      };
      reader.readAsDataURL(file);
    }
  };

  return (
    <div className='InputButton'>
      <label for="InputGambar">
        <p>
          Insert Image
        </p>
        <input type="file" id="InputGambar" accept="image/*" onChange={handleFileChange} />
      </label>
    </div>
  );
};

export default InputPicture;
