import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const RedirectButton = () => {
  const [destination, setDestination] = useState('');
  const navigate = useNavigate();

  const handleInputChange = (e) => {
    setDestination(e.target.value);
  };

  const handleClick = () => {
    if (destination) {
      navigate(destination);
    }
  };

  return (
    <div>
      <input type="text" placeholder="Enter destination" onChange={handleInputChange} />
      <button onClick={handleClick}>
        Go to {destination || '...'}
      </button>
    </div>
  );
};

export default RedirectButton;
