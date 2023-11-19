import React from 'react';
import deleteLastLogo from '../Assets/DeleteLast.jpg'; // Replace with the actual path to your logo

function AboutUs() {
    return (
        <div className="AboutUs">
            <h2 className="Header">About Us</h2>
            <p className='Text'>
                Website ini dibuat oleh kelompok DeleteLast yang beranggotakan
                Muhammad Nugraha Eka Prawira (13522001), Ahmad Farid Mudrika (13522008), dan
                Zachary Samuel Tobing (13522016) untuk pengerjaan Tugas Besar Aljabar Linear dan Geometri.
            </p>
            <img src={deleteLastLogo} alt="DeleteLast Logo" className="Logo" />
        </div>
    );
}

export default AboutUs;
