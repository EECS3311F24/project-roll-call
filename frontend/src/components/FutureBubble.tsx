import { useState, useEffect } from 'react';
import axios from 'axios';
import { CalendarEvent } from '../types';

function FutureBubble() {
    const [futureEvents, setFutureEvents] = useState<{type: string, events: CalendarEvent[]}[]>([]);
    const [error, setError] = useState<string | null>(null); // Add error state for better debugging

    const fetchFutureEvents = async () => {
        try {
            const response = await axios.get('http://localhost:5000/cal/future_events', {
                withCredentials: true, // Ensure credentials like cookies are sent
            });
            setFutureEvents(response.data); // Update state with fetched data
            setError(null); // Reset error state on success
        } catch (error: any) {
            console.error("Error fetching future events:", error.response?.data || error.message);
            setError(error.response?.data || error.message); // Store the error for display
        }
    };

    // Fetch events when the component mounts
    useEffect(() => {
        fetchFutureEvents();
    }, []);

    return (
        <div
            className="mb-3 mx-2 border rounded-[30px] bg-[#CDBACF] transition-transform duration-300 transform hover:scale-105 flex flex-col overflow-hidden"
            style={{
                height: 'calc(100vh - 350px)',
            }}
        >
            {/* Title */}
            <div className="mt-5 text-lg text-center font-bold">Future at a Glance</div>

            <div className="mx-3 mb-7 mt-3 mr-4 flex-1 overflow-y-auto scrollbar-thin scrollbar-thumb-rounded-full scrollbar-track-rounded-full scrollbar scrollbar-thumb-[#ac8db0]">

                
                {/* Render fetched events */}
                {futureEvents.map((eventGroup) => (
                    <div key={eventGroup.type} className="mb-2">
                        <h2 className="mx-1 text-black font-bold">{eventGroup.type}</h2>

                        {eventGroup.events.map(event => (
                            <div key={event.id} className="ml-3 pr-1 flex items-start">
                                <span className="font-semibold text-gray-700 whitespace-nowrap">
                                    ‣ &nbsp;{event.day}:
                                </span>
                                <span className="ml-2 flex-1">{event.summary}</span>
                            </div>
                        ))}
                    </div>
                ))}
            </div>
        </div>
    );
}

export default FutureBubble;
