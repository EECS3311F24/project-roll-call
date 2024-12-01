import * as React from 'react';
import dayjs from "dayjs";
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { StaticTimePicker } from '@mui/x-date-pickers/StaticTimePicker';

export default function TimeBubble() {
  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      <StaticTimePicker 
      orientation="landscape"
      localeText={{
        cancelButtonLabel: 'Cancel',  // Example of another label you can customize
        okButtonLabel: 'Ok',         // Custom button text for ok
      }}
      //size of white background
      sx={{ // Adjust the height of the entire picker
        borderRadius: 5,

        '& .MuiClock-root': {
          transform: 'scale(0.8)', // Enlarge the clock         
        },
        //Pointer 
        '& .MuiClock-pin': {
          height: '10px', // Customize the size of the clock pin
          width: '10px',
          backgroundColor: '#32A6F9',
        },
        '& .MuiClockPointer-root': {
            width: '2px', // Adjust the pointer arm thickness
            backgroundColor: '#32A6F9', // Change the color of the pointer arm
          },
        '& .MuiClockPointer-thumb': {
          borderColor: '#32A6F9',
          backgroundColor: '#32A6F9',
        },  
                  
        
      }}
      slotProps={{
        rightArrowIcon: {
          sx: {
            color: '#32A6F9', // Set the arrow color to blue
          },
        },
        leftArrowIcon: {
          sx: {
            color: '#32A6F9', // Set the arrow color to blue
          },
        },
        actionBar: {
            sx: {
              '& .MuiButton-root': {
                color: '#32A6F9', // Default color for buttons
                fontSize: '14px',
                fontWeight: '500',
              },
            },
        }, 
      }}
      />
    </LocalizationProvider>
  );
}
