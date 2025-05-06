import './App.css';
import { useState } from 'react';
import Header from './components/Header';
import Form from './components/Form';
import Report from './components/Report';

function App() {
  const [pat, setPat] = useState('');
  const [report, setReport] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isError, setIsError] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      setIsLoading(true);
      setIsError(false);
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
      setIsLoading(false);
    } catch (error) {
      console.error('Error:', error);
      setIsError(true);
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <Header isLoading={isLoading} isError={isError}/>
      <Form pat={pat} setPat={setPat} handleSubmit={handleSubmit} />
      {report && <Report report={report} />}
    </div>
  );
}

export default App;
