import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';
import { DataTypeA, CalendarEvent } from './types';

function App() {
  const [data, setData] = useState<DataTypeA[]>([]);
  const [firstName, setField1] = useState('');
  const [lastName, setField2] = useState('');
  const [events, setEvents] = useState<CalendarEvent[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get('http://localhost:5000/api/data');
      setData(response.data);
    }
    fetchData();
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const newItem = { firstName, lastName };
    const response = await axios.post('http://localhost:5000/api/data', newItem);
    setData([...data, response.data]);
    setField1('');
    setField2('');
  };

  useEffect(() => {
    const fetchEvents = async () => {
      const response = await axios.get('http://127.0.0.1:5000/api/events');
      setEvents(response.data);
    };
    fetchEvents();
  }, []);

  return (
    <div>
      <h1>Upcoming Events</h1>
      {events.length === 0 ? (<p>No upcoming events found.</p>) : (
        <ul>
            {events.map((event) => (
                <li key={event.id}>
                    {event.start.dateTime || event.start.date}: {event.summary}
                </li>
            ))}
        </ul>
      )}
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
            onChange={e => setField1(e.target.value)}
            required
          />
        </p>
        <p>
          Last Name
          <input
            type="text"
            value={lastName}
            onChange={e => setField2(e.target.value)}
            required
          />
        </p>
        <button type="submit">Submit</button>
      </form>
    </div>
  )
}

export default App
