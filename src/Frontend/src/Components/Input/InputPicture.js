import axios from 'axios';

const InputPicture = ({ onImageSelect }) => {
  const handleFileChange = async (event) => {
    const file = event.target.files[0];

    if (file) {
      const formData = new FormData();
      formData.append('file', file);
      const reader = new FileReader();
      reader.onloadend = () => {
        const imageData = reader.result;
        onImageSelect(imageData);
      };

      try {
        const response = await axios.post(
          'http://127.0.0.1:8000/api/upload/single/',
          formData,
          {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
          }
        );

        const imageData = response.data.imageData;
        onImageSelect(imageData);
      } catch (error) {
        console.error('Error uploading image:', error);
      }
      reader.readAsDataURL(file);
    }
  };

  return (
    <div className='InputButton'>
      <label for="InputGambar">
        <span className='InsertImageText'>
          Insert Image
        </span>
        <input type="file" id="InputGambar" accept="image/*" onChange={handleFileChange} />
      </label>
    </div>
  );
};

export default InputPicture;
