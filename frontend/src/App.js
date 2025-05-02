import './App.css';
import { useState } from 'react';
import Header from './components/Header';
import Form from './components/Form';
import Report from './components/Report';

function App() {
  const [pat, setPat] = useState('');
  const [report, setReport] = useState(null);

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
      setPat('');
      setReport(data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="App">
      <Header />
      <Form pat={pat} setPat={setPat} handleSubmit={handleSubmit} />
      {report && <Report report={report} />}
    </div>
  );
}

export default App;
