import { useState, useEffect } from 'react';
import axios from 'axios';
import { CalendarEvent } from '../types';
import { formatTime } from '../utility/dateUtils';

function WeekBubble() {
    const [weekEvents, setWeekEvents] = useState<{ day: string; events: CalendarEvent[] }[]>([]);
    const [error, setError] = useState<string | null>(null); // Add error handling for better debugging

    const fetchWeekEvents = async () => {
        try {
            const response = await axios.get('http://localhost:5000/cal/week_events', {
                withCredentials: true, // Ensures credentials (like cookies) are sent
            });
            setWeekEvents(response.data);
            setError(null); // Clear error on successful fetch
            console.log("Fetched week events: ", response.data);
        } catch (error: any) {
            console.error("Error fetching week events:", error.response?.data || error.message);
            setError(error.response?.data || error.message); // Store error for display
        }
    };

    useEffect(() => {
        fetchWeekEvents();
    }, []); // Runs once on mount

    return (
        <div
            className="mb-3 mx-2 border rounded-[30px] bg-[#a4cc8f] transition-transform duration-300 transform hover:scale-105 flex flex-col overflow-hidden"
            style={{
                height: 'calc(100vh - 350px)',
            }}
        >
            <div className="mt-5 text-lg text-center font-bold">Upcoming This Week</div>

            <div className="mx-3 mb-7 mt-3 mr-4 flex-1 overflow-y-auto scrollbar-thin scrollbar-thumb-rounded-full scrollbar-track-rounded-full scrollbar scrollbar-thumb-[#83ba67]">

                {/* Display events */}
                {weekEvents.map((day) => (
                    day.events.length > 0 && (
                        <div key={day.day} className="mb-4">
                            <h2 className="mx-2 text-black font-bold">{day.day}</h2>
                            {day.events.map((event) => (
                                <div key={event.id} className="ml-5 flex items-start">
                                    <span className="font-semibold text-gray-700 whitespace-nowrap">
                                        ‣ &nbsp;{event.start.dateTime ? formatTime(event.start.dateTime) : 'All Day'}:
                                    </span>
                                    <span className="ml-2 flex-1">{event.summary}</span>
                                </div>
                            ))}
                        </div>
                    )
                ))}
            </div>
        </div>
    );
}

export default WeekBubble;
