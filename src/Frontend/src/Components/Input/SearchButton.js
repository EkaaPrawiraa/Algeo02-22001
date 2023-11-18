
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
    <div className='Sementara'>
      <div className="SearchButton"  style={{ position: 'absolute', right : 320, top : 500, }}>
        <button className="Features" id="Search" onClick={handleSearchClick}>
          Search
        </button>
      </div>
      <div className="Result">
        <h2>Search Results:</h2>
        {searchResults && searchResults.length === 0 ? (
          <p>No results found</p>
        ) : (
            <ImageOutput images={searchResults} totalTime={searchtime} />
        )}
      </div>
    </div>
  );
}


export default Search;
