import React, { useState, useEffect } from 'react';

const ImageOutput = ({ images }) => {
  const [currentPage, setCurrentPage] = useState(1);
  const imagesPerPage = 6;
  const totalImages = images.length;
  const totalPages = totalImages > 0 ? Math.ceil(totalImages / imagesPerPage) : 0;

  const paginatedImages = images.slice((currentPage - 1) * imagesPerPage, currentPage * imagesPerPage);

  const handleNextPage = () => {
    setCurrentPage((prevPage) => Math.min(prevPage + 1, totalPages));
  };

  const handlePrevPage = () => {
    setCurrentPage((prevPage) => Math.max(prevPage - 1, 1));
  };

  useEffect(() => {
    setCurrentPage(1);
  }, [images]);

  return (
    <div className='Pagination'>
      <div className='ImageRow'>
        {paginatedImages.map((image, index) => (
          <div key={index} className="ImageContainer" style={{ display: 'inline-block', margin: '10px' }}>
            <img src={URL.createObjectURL(image)} alt={`Img ${index + 1}`} className='Image' style={{ maxWidth: '100%' }} />
            <p>Persentase</p>
          </div>
        ))}
      </div>
      <div className='PrevNext'>
        <button className="Prev" onClick={handlePrevPage} disabled={currentPage === 1}>
          Previous Page
        </button>
        <span className='Page'> Page {currentPage} of {totalPages} </span>
        <button className="Next" onClick={handleNextPage} disabled={currentPage === totalPages}>
          Next Page
        </button>
      </div>
    </div>
  );
};

export default ImageOutput;
