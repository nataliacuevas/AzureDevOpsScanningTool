import React from 'react';
import './Header.css'; // Import the CSS file

function Header() {
  return (
    <header className="header-container">
      <img src="/pfLogo.svg" className="header-logo" alt="logo" />
      <p className="header-text">
        PrimeFaktor Azure DevOps Security Analyzer <br />
        Please Provide a PAT
      </p>
    </header>
  );
}

export default Header;
