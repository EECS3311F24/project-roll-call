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
    end: {
        dateTime?: string;
        date?: string; 
    }
    colorId?: string;
    status?: string;
    day?: string;
}

export interface EventSettings {
    category: string;
    color: number;
    priority: string;
}
  
export interface Settings {
    greeting: string;
    future_weeks: number;
    organize_by: string;
    e1: EventSettings;
    e2: EventSettings;
    e3: EventSettings;
    e4: EventSettings;
    e5: EventSettings;
    e6: EventSettings;
    e7: EventSettings;
    e8: EventSettings;
    e9: EventSettings;
    e10: EventSettings;
    e11: EventSettings;
    notification: boolean;
    notification_time: string;
}

export interface SwitchWQProps {
    greeting: string;
    toggleGreeting: () => void;
}

export interface SwitchCPProps {
    organize_by: string;
    toggleOrganize: () => void;
}

export interface SwitchYesNoProps {
    notification: boolean;
    toggleNotification: () => void;
}

export interface AutoCompleteCEProps {
    label: string;
    onSelectionChange: (newValue: string) => void;
}

export interface AutoCompletePrioProps {
    label: string;
    onSelectionChange: (newValue: string) => void;
}