import React, { useEffect, useState } from 'react';
import axios from 'axios';

function DataVisualizer() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('/api/analyze').then(res => {
      setData(res.data.prediction);
    });
  }, []);

  return (
    <div>
      <h1>Data Visualization</h1>
      <p>Prediction: {data}</p>
    </div>
  );
}

export default DataVisualizer;