
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import ImageOutput from '../Output/ImageOutput';

function Search({ selectedToggle }) {
  const [searchResults, setSearchResults] = useState([]);
  const [searchtime, setSearchtime] = useState([]);
  const [isSearchTriggered, setIsSearchTriggered] = useState(false);

  useEffect(() => {
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
          setSearchtime(response.data.total_time || 0); 
          setIsSearchTriggered(false);
        }
      } catch (error) {
        console.error('Error searching:', error);
      }
    };

    fetchData();
  }, [selectedToggle, isSearchTriggered]);

  const handleSearchClick = () => {
    setIsSearchTriggered(true);
  };
  return (
    <div>
      <div className="SearchButtonContainer">
        <button
          className="SearchButton"
          id="Search"
          onClick={handleSearchClick}
          style={{ color: 'white' }}
        >
          Search
        </button>
      </div>

      <div className="ResultContainer" style={{ position: 'absolute', left: 100, top: 700 }}>
        <h2 style={{ left: 100, top: 1500 }}>Search Results: </h2>
        {searchResults && searchResults.length === 0 ? (
          <p>No results found
            <ol> Total time : {searchtime} seconds</ol>
          </p>
        ) : (
          <ImageOutput images={searchResults} totalTime={searchtime} />
        )}
      </div>
    </div>
  );
}

export default Search;
