import { useState, useEffect } from 'react';
import axios from 'axios';
import { CalendarEvent } from '../types';
import { formatTime } from '../utility/dateUtils';

// Component which displays the google events for the day on today page. It organizes the events based on Morning, Afternoon and evening.
// events which have passed will be faded and events which are happening now will be highlighted in blue
function TodayBubble() {
  const [dayEvents, setDayEvents] = useState<{
    allDay: CalendarEvent[];
    morning: CalendarEvent[];
    afternoon: CalendarEvent[];
    evening: CalendarEvent[];
  }>({
    allDay: [],
    morning: [],
    afternoon: [],
    evening: []
  });

  useEffect(() => {
    const fetchDayEvents = async () => {
      const response = await axios.get('http://127.0.0.1:5000/day_events');
      setDayEvents(response.data);
    };
    fetchDayEvents();
    console.log(dayEvents);
  }, []);

  const areAllEventsPast = (events: CalendarEvent[]) => {
    return events.every((event) => event.status === "past");
  };

  const renderEvents = (title: string, events: CalendarEvent[]) => (
    <div className={`mb-4`}>
      <h2 className={`mx-2 font-bold ${areAllEventsPast(events) ? 'opacity-40' : 'text-black'}`}>{title}</h2>  
      {events.map((event) => {
        const isAllDay = event.start.date && !event.start.dateTime;

        return(
          <div key={event.id} className={`ml-4 flex items-start ${event.status === "past" ? 'opacity-40' : ''}`}>
            <span className={`font-semibold whitespace-nowrap ${event.status === "ongoing" ? 'text-blue-600' : 'text-gray-700'}`}>
              ‣ &nbsp;{isAllDay ? '' : formatTime(event.start.dateTime || '') + ':'}
            </span>
            <span className={`ml-2 flex-1 font-normal whitespace-normal ${event.status === "ongoing" ? 'text-blue-600' :  'text-black-700'}`}
            style={isAllDay ? { marginLeft: '0px' } : {}}>
              {event.summary}
            </span>
          </div>
        );
      })}
    </div>
  );

  return (
    <div
      className="mb-3 mx-2 border rounded-[30px] bg-[#F2B391] transition-transform duration-300 transform hover:scale-105 flex flex-col overflow-hidden"
      style={{
          height: 'calc(100vh - 350px)', // Subtract space for navbar and margins
      }}
    >
      <div className="mt-5 text-lg text-center font-bold">Up on the Agenda Today</div>
      <div className="mx-3 mb-7 mt-3 mr-4 flex-1 overflow-y-auto scrollbar-thin scrollbar-thumb-rounded-full scrollbar-track-rounded-full scrollbar scrollbar-thumb-[#ec8f5c]">
        {dayEvents.allDay.length > 0 && renderEvents('All Day', dayEvents.allDay)}
        {dayEvents.morning.length > 0 && renderEvents('Morning', dayEvents.morning)}
        {dayEvents.afternoon.length > 0 && renderEvents('Afternoon', dayEvents.afternoon)}
        {dayEvents.evening.length > 0 && renderEvents('Evening', dayEvents.evening)}
      </div>
    </div>
  );
}

export default TodayBubble;
