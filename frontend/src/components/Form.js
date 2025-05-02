import React from 'react';
import './Form.css'; // Import the CSS file

function Form({ pat, setPat, handleSubmit }) {
  return (
    <form onSubmit={handleSubmit} className="form-container">
      <input
        type="password"
        placeholder="Enter your PAT"
        value={pat}
        onChange={(e) => setPat(e.target.value)}
        className="form-input"
      />
      <button type="submit" className="form-button">
        Send PAT
      </button>
    </form>
  );
}

export default Form;
