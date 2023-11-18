// ColorTextureToggle.js
import React, { useState } from 'react';
import Search from './SearchButton';

function ColorTextureToggle() {
  const [selectedToggle, setSelectedToggle] = useState('Color');

  const handleToggleChange = () => {
    setSelectedToggle(selectedToggle === 'Color' ? 'Texture' : 'Color');
  };

  return (
    <span className="ColorTextureToggle" >
      <span className="SubColorTextureToggle" style={{ position: 'absolute', right : 230, top : 370, }}>
        <p className="ColorTitle">Color</p>
        <input
          type="checkbox"
          id="switch"
          className="checkbox"
          onChange={handleToggleChange}
          checked={selectedToggle === 'Texture'}
        />
        <label htmlFor="switch" className="toggle">
          <p></p>
        </label>
        <p className="TextureTitle">Texture</p>
      </span>
      {/* Pass the selectedToggle as a prop to the Search component */}
      <Search selectedToggle={selectedToggle} />
    </span>
  );
}

export default ColorTextureToggle;
