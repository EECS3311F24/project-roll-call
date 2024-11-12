import { useState, useEffect } from 'react';
import axios from 'axios';
import { CalendarEvent } from '../types';
import { formatTime } from '../utility/dateUtils';
import { getEventType } from '../utility/eventUtils';

function FutureBubble() {
    const [FutureEvents, setFutureEvents] = useState<CalendarEvent[]>([]);

    useEffect(() => {
        const fetchFutureEvents = async () => {
            const response = await axios.get('http://127.0.0.1:5000/future_events');
            setFutureEvents(response.data);
        };
        fetchFutureEvents();
    }, []);

    // Group events by type
    const eventsByType: Record<string, CalendarEvent[]> = {};
    FutureEvents.forEach(event => {
        const eventType = getEventType(event);
        if (!eventsByType[eventType]) {
            eventsByType[eventType] = [];
        }
        eventsByType[eventType].push(event);
    });
    

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
                
                {Object.entries(eventsByType).map(([type, events]) => (
                    <div key={type} className="mb-2">
                        <h2 className="mx-1 text-black font-bold">{type.charAt(0).toUpperCase() + type.slice(1)}</h2>
                        {events.map(event => (
                            <div key={event.id} className="ml-5 pr-1 flex items-start">
                                <span className="font-semibold text-gray-700 whitespace-nowrap">
                                    ‣ &nbsp;{event.start.dateTime 
                                        ? new Date(event.start.dateTime).toLocaleDateString('en-US', {month: 'short', day: 'numeric' }) 
                                        : event.start.date 
                                        ? new Date(event.start.date).toLocaleDateString('en-US', {month: 'short', day: 'numeric' }) 
                                        : ''}:
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