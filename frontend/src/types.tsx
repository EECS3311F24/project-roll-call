export interface DataTypeA{
    _id: string;
}

export interface CalendarEvent {
    id: string;
    summary: string;
    start: {
        dateTime?: string;
        date?: string; 
    };
}