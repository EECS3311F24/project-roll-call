import { useState, useEffect } from 'react';
import axios from 'axios';
import { CalendarEvent } from '../types';
import { formatTime } from '../utility/dateUtils';

function WeekBubble() {
    const [weekEvents, setWeekEvents] = useState<CalendarEvent[]>([]);

    useEffect(() => {
        const fetchWeekEvents = async () => {
        const response = await axios.get('http://127.0.0.1:5000/week_events');
        setWeekEvents(response.data);
        };
        fetchWeekEvents();
    }, []);

    const daysOfWeek = [];
    for (let i = 0; i < 6; i++) {
        const date = new Date();
        date.setDate(date.getDate() + 1 + i);
        const label = date.toLocaleDateString('en-US', {weekday: 'long', month: 'short', day: 'numeric',});

        daysOfWeek.push({ date: date, label: label });
    }

    const eventsByDay: CalendarEvent[][] = []
    for (let i = 0; i < daysOfWeek.length; i++) {
        const day = daysOfWeek[i];
        const dayStart = new Date(day.date);
        dayStart.setHours(0, 0, 0, 0);
        const dayEnd = new Date(day.date);
        dayEnd.setHours(23, 59, 59, 999);

        const eventsForThisDay = weekEvents.filter(event => {
            const eventDate = new Date(event.start.dateTime || '');
            return eventDate >= dayStart && eventDate <= dayEnd;
        });

        eventsByDay.push(eventsForThisDay);
    }

    return (
        <div className="grid gap-2" style={{ gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))' }}>
        <div className="mx-2 border rounded-[30px] h-[420px] transition-transform duration-300 transform hover:scale-105 bg-[#a4cc8f]">
            <div className="mt-5 text-lg text-center font-bold">Up on the Agenda This Week</div>
            <div className="mx-3 mt-3 h-[330px] overflow-y-auto">
            {daysOfWeek.map((day, index) => (
                eventsByDay[index].length > 0 && (
                <div key={day.label} className="mb-4">
                    <h2 className="mx-2 text-black font-bold">{day.label}</h2>
                    {eventsByDay[index].map(event => (
                    <div key={event.id} className="ml-5 flex items-start">
                        <span className="font-semibold text-gray-700 whitespace-nowrap">‣ &nbsp;{formatTime(event.start.dateTime || '')}:</span>
                        <span className="ml-2 flex-1">{event.summary}</span>
                    </div>
                    ))}
                </div>
                )
            ))}
            </div>
        </div>
        </div>
    );
}

export default WeekBubble;