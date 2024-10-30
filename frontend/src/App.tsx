import { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';
import { CalendarEvent } from './types';

function App() {
  const [dayEvents, setDayEvents] = useState<CalendarEvent[]>([]);
  // const [weekEvents, setWeekEvents] = useState<CalendarEvent[]>([]);

  useEffect(() => {
    const fetchDayEvents = async () => {
      const response = await axios.get('http://127.0.0.1:5000/day_events');
      setDayEvents(response.data);
    };
    fetchDayEvents();
  }, []);

  // useEffect(() => {
  //   const fetchWeekEvents = async () => {
  //     const response = await axios.get('http://127.0.0.1:5000/week_events');
  //     setWeekEvents(response.data);
  //   };
  //   fetchWeekEvents();
  // }, []);

  return (
    <div>
      <h1>Upcoming Events for Today</h1>
      <ul>
        {dayEvents.map((event) => (
            <li key={event.id}>{event.start.dateTime || event.start.date}: {event.summary}</li>
        ))}
      </ul>
      {/* <h1>Upcoming Events for This Week</h1>
      <ul>
        {weekEvents.map((event) => (
            <li key={event.id}>{event.start.dateTime || event.start.date}: {event.summary}</li>
        ))}
      </ul> */}
    </div>
  )
}

export default App
