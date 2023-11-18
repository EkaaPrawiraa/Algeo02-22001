// Search.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import ImageOutput from '../Output/ImageOutput';

function Search({ selectedToggle }) {
  const [searchResults, setSearchResults] = useState([]);
  const [searchtime, setSearchtime] = useState([]);
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
          setSearchResults(response.data.processed_images || []);
          setSearchtime(response.data.total_time) // Assuming 'processed_images' is the key in the response
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
        <span className="Features" onClick={handleSearchClick}>
          Search
        </span>
      </div>
      <div className="SearchResults">
        <h2>Search Results:</h2>
        {searchResults && searchResults.length === 0 ? (
          <p>No results found</p>
        ) : (
          <ul>

                <ImageOutput images={searchResults} totalTime={searchtime} />
                {/* Display other properties or image data if needed */}
              )
          </ul>
        )}
      </div>
    </div>
  );
}

export default Search;
