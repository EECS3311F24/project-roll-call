import { useState, useEffect } from 'react';
import axios from 'axios';
import { CalendarEvent } from '../types';
import { formatTime } from '../utility/dateUtils';

function FutureBubble() {
    const [weekEvents, setWeekEvents] = useState<CalendarEvent[]>([]);

    useEffect(() => {
        const fetchFutureEvents = async () => {
            const response = await axios.get('http://127.0.0.1:5000/future_events');
            setWeekEvents(response.data);
        };
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

            {/* Content */}
            <div className="mx-3 mb-7 mt-3 flex-1 overflow-y-auto">
                {weekEvents.length > 0 ? (
                    weekEvents.map((event) => (
                        <div key={event.id} className="mb-4 flex items-start">
                            <span className="font-semibold text-gray-700 whitespace-nowrap">
                                ‣ &nbsp;{formatTime(event.start.dateTime || '')}:
                            </span>
                            <span className="ml-2 flex-1">{event.summary}</span>
                        </div>
                    ))
                ) : (
                    <div className="text-center text-gray-500">No events scheduled.</div>
                )}
            </div>
        </div>
    );
}

export default FutureBubble;