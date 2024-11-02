import { useState, useEffect } from 'react';
import axios from 'axios';
import { CalendarEvent } from '../types';
import { formatTime } from '../utility/dateUtils';

function WeekBubble() {
    const [weekEvents, setWeekEvents] = useState<CalendarEvent[]>([]);

    useEffect(() => {
        const fetchDayEvents = async () => {
        const response = await axios.get('http://127.0.0.1:5000/day_events');
        setWeekEvents(response.data);
        };
        fetchDayEvents();
    }, []);


  return (
    <>
    <div className="grid gap-2" style={{ gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))' }}>

        <div className="mx-2 border rounded-[30px] h-[420px] transition-transform duration-300 transform hover:scale-105 bg-[#A4CC8F]">
            <div className="my-5 text-lg text-center font-semibold">
            Upcoming Week
        </div>

        <div className="mt-2 text-sm">
            <ul className="space-y-2">
                {weekEvents.map((event) => (
                <li 
                    key={event.id} 
                    className="flex items-center p-2 border-b border-gray-200 last:border-b-0" 
                >
                    <span className="mx-3 text-black-600"> ★</span> 
                    <span className="font-semibold">{event.start.dateTime || event.start.date}</span>
                    <span className="ml-2 text-gray-700">{event.summary}</span> 
                </li>
                ))}
            </ul>
        </div>
      </div>
    </div>
    </>
  );
}

export default WeekBubble;