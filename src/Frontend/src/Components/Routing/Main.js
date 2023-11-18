import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Home from '../Pages/Home';
import BriefConcept from '../Pages/BriefConcept';
import HowToUse from '../Pages/HowToUse';
import AboutUs from '../Pages/AboutUs';

const Main = () => {
  return (
    <div className='Main'>
        <Router>
            <nav>
                <div className="NavBar">
                    <Link to ="/" className='Nav' id='Nav1'>Home</Link>
                    <Link to ="/BriefConcept" className='Nav' id='Nav2'>Brief Concept</Link>
                    <Link to ="/HowToUse" className='Nav' id='Nav3'>How to Use</Link>
                    <Link to="/AboutUs" className='Nav' id='Nav4'>About Us</Link>
                </div>
            </nav>
            <Routes>
                <Route path="/" element={<Home></Home>} />
                <Route path="/BriefConcept" element={<BriefConcept></BriefConcept>} />
                <Route path="/HowToUse" element={<HowToUse></HowToUse>} />
                <Route path="/AboutUs" element={<AboutUs></AboutUs>} />
            </Routes>
        </Router>
    </div>
  );
};

export default Main;
