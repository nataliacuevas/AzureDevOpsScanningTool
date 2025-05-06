import React from 'react';
import './Header.css'; // Import the CSS file

function Header({ isLoading, isError }) {
  return (
    <header className="header-container">
      <img 
        src={isError ? "/pfLogoError.svg" : "/pfLogo.svg"} 
        className={isLoading ? "header-logo-spin" : "header-logo"}
        alt="logo" 
      />
      <p className="header-text">
        PrimeFaktor Azure DevOps Security Analyzer <br />
        Please Provide a PAT
      </p>
      <div className='h6vmin'>
      <p className={isLoading ? "header-text" : "hidden-header-text"}>
           Loading...
        </p>        
        <p className={isError ? "header-text" : "hidden-header-text"}>
           Error!
        </p>
      </div>
     
    </header>
  );
}

export default Header;
