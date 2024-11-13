import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';
import { DataTypeA } from './types';

function App() {
  // State to hold data fetched from the server, initially an empty array
  const [data, setData] = useState<DataTypeA[]>([]);
  // State to hold the input value for firstName
  const [firstName, setField1] = useState('');
  // State to hold the input value for lastName
  const [lastName, setField2] = useState('');

  // useEffect hook to fetch data when the component first mounts
  useEffect(() => {
    // Function to fetch data asynchronously
    const fetchData = async () => {
      // Make a GET request to the server to fetch data
      const response = await axios.get('http://localhost:5000/api/data');
      // Update the data state with the fetched data
      setData(response.data);
    }

    // Call fetchData when the component mounts
    fetchData();
  }, []); // Empty dependency array means this runs only once on mount

  // Function to handle form submission
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault(); // Prevent default form submission behavior
    // Create a new object using the first and last name values
    const newItem = { firstName, lastName };
    // Make a POST request to add the new item to the server
    const response = await axios.post('http://localhost:5000/api/data', newItem);
    // Add the new item to the "data" state to update the list in the UI
    setData([...data, response.data]);
    // Clear the input fields by resetting their states
    setField1('');
    setField2('');
  };

  return (
    <div>
      <h1>Data from MongoDB</h1>
      <p>
        {data.map(item => (
          <li key={item._id}>{JSON.stringify(item)}</li>
        ))}
      </p>
      <form onSubmit={handleSubmit}>
        <p>
          First Name
          <input
            type="text"
            value={firstName}
            onChange={e => setField1(e.target.value)} // Update firstName state on input change
            required
          />
        </p>
        <p>
          Last Name
          <input
            type="text"
            value={lastName}
            onChange={e => setField2(e.target.value)} // Update lastName state on input change
            required
          />
        </p>
        <button type="submit">Submit</button>
      </form>
    </div>
  )
}

export default App
