// Search.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Search({ selectedToggle }) {
  const [searchResults, setSearchResults] = useState([]);
  const [isSearchTriggered, setIsSearchTriggered] = useState(false);

  useEffect(() => {
    // Perform different actions based on the selectedToggle prop
    const fetchData = async () => {
      try {
        if (isSearchTriggered) {
          let response;
          if (selectedToggle === 'Color') {
            response = await axios.get('http://localhost:8000/api/process-color-images/');
            console.log('Searching color...');
          } else if (selectedToggle === 'Texture') {
            response = await axios.get('http://localhost:8000/api/process-images/');
            console.log('Searching texture...');
          }
          setSearchResults(response.data.processed_images || []); // Assuming 'processed_images' is the key in the response
          setIsSearchTriggered(false); // Reset the search trigger after fetching data
          // Add your new action or program here
          // ...
        }
      } catch (error) {
        console.error('Error searching:', error);
      }
    };

    fetchData();
  }, [selectedToggle, isSearchTriggered]);

  const handleSearchClick = () => {
    // Trigger the search by updating the state
    setIsSearchTriggered(true);
  };

  return (
    <div>
      <div className="SearchButton">
        <button className="Features" id="Search" onClick={handleSearchClick}>
          Search
        </button>
      </div>
      <div className="SearchResults">
        <h2>Search Results:</h2>
        {searchResults.length === 0 ? (
          <p>No results found</p>
        ) : (
          <ul>
            {searchResults.map((result, index) => (
              <li key={index}>
                <p>Image Name: {result.image_name}</p>
                <p>Percentage: {result.percentage}</p>
                {/* Display other properties or image data if needed */}
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}

export default Search;
