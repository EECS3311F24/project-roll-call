
// a function which formats the time string returned from the google api to a more beautiful one: (11:00 AM)
export function formatTime(dateTime: string): string {

    const date = new Date(dateTime);
    let hours = date.getHours();
    const minutes = date.getMinutes();
    const ampm = hours >= 12 ? 'PM' : 'AM';
  
    hours = hours % 12;
    hours = hours ? hours : 12; // Adjust 0 hours to 12
    const minutesStr = minutes < 10 ? `0${minutes}` : minutes; // Pad minutes
  
    return `${hours}:${minutesStr} ${ampm}`;
}



