import './App.css';
import { useState } from 'react';

function App() {
  const [pat, setPat] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/api/message', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ PAT: pat }),
      });
      const data = await response.json();
      console.log(data);
      setPat(''); // Clear the input field after submission
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src="/pfLogo.svg" className="App-logo" alt="logo" />
        <p>
          PrimeFaktor Azure DevOps Security Analyzer <br/>
          Please Provide a PAT
        </p>
        <form onSubmit={handleSubmit}>
          <input
            type="password"
            placeholder="Enter your PAT"
            value={pat}
            onChange={(e) => setPat(e.target.value)}
          />
          <button type="submit">Send PAT</button>
        </form>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
