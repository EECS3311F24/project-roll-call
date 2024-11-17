import { useState, useEffect } from 'react';
import axios from 'axios';
import { CalendarEvent } from '../types';
import { formatTime } from '../utility/dateUtils';

function TodoBubble() {
    const [weekEvents, setWeekEvents] = useState<CalendarEvent[]>([]);
    const [completedTasks, setCompletedTasks] = useState<{ [key: string]: boolean }>({}); // Track completed tasks

    useEffect(() => {
        const fetchToDo = async () => {
            const response = await axios.get('http://127.0.0.1:5000/to_do');
            setWeekEvents(response.data);
        };
        fetchToDo();
    }, []);

    // Toggle the completion status of a task
    const toggleTaskCompletion = (id: string) => {
        setCompletedTasks((prevState) => ({
            ...prevState,
            [id]: !prevState[id], // Toggle the completed status
        }));
    };

    return (
        <div
            className="mb-3 mx-2 border rounded-[30px] bg-[#85D4FF] transition-transform duration-300 transform hover:scale-105 flex flex-col overflow-hidden"
            style={{
                height: 'calc(100vh - 350px)',
            }}
        >
            {/* Title */}
            <div className="mt-5 text-lg text-center font-bold">Suggested To-Do</div>

            {/* Content */}
            <div className="mx-3 mb-7 mt-3 flex-1 overflow-y-auto pl-3">
                {weekEvents.length > 0 ? (
                    weekEvents.map((event) => (
                        <div
                            key={event.id}
                            className={`mb-4 flex items-start ${
                                completedTasks[event.id] ? 'text-gray-500 line-through' : ''
                            }`}
                        >
                            <input
                                type="checkbox"
                                checked={completedTasks[event.id] || false}
                                onChange={() => toggleTaskCompletion(event.id)}
                                className="mt-1 mr-2"
                            />
                            <span className="flex-1">{event.summary}</span>
                        </div>
                    ))
                ) : (
                    <div className="text-center text-gray-500">No events scheduled.</div>
                )}
            </div>
        </div>
    );
}

export default TodoBubble;