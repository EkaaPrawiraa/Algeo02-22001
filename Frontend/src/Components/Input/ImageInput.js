import DisplayPicture from "./DisplayPicture";
import ColorTextureToggle from "./ColorTextureToggle";
import InputPicture from "./InputPicture";
import Search from "./SearchButton";
import { useState } from "react";
const ImageInput = () => {
    const [selectedImage, setSelectedImage] = useState(null);
  
    const handleImageSelect = (imageData) => {
      setSelectedImage(imageData);
    };
  
    return (
      <div className="ImageInput">
        <InputPicture onImageSelect={handleImageSelect} />
        {selectedImage && <DisplayPicture imageData={selectedImage} />}
        <ColorTextureToggle></ColorTextureToggle>
        
      </div>
    );
  };
  
  export default ImageInput;