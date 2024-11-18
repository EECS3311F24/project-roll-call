import { CalendarEvent } from '../types';


// return the event type based on color
export function getEventType(event: CalendarEvent): string {

    if (event.colorId === "11") {
        return "Deadlines & Assessments";
    }
    if (event.colorId === "6") {
        return "Appointments";
    }
    if (event.colorId === "10") {
        return "Works";
    }
    if (event.colorId === "9") {
        return "Workouts";
    }
    if (event.colorId === "1") {
        return "Social Events";
    }
    if (event.colorId === "3") {
        return "Unique Events";
    }

    return "Class/Meeting";
}