import * as React from 'react';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { StaticTimePicker } from '@mui/x-date-pickers/StaticTimePicker';

export default function StaticTimePickerLandscape() {
  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      <StaticTimePicker orientation="landscape" 
      
      localeText={{
        cancelButtonLabel: 'Cancel',  // Example of another label you can customize
        okButtonLabel: 'Ok',         // Custom button text for ok
      }}
      //size of white background
      sx={{
        width: 500, // Adjust the width of the entire picker
        height: 300, // Adjust the height of the entire picker
        borderRadius: 5,
      }}
      slotProps={{
        rightArrowIcon: {
          sx: {
            color: '#32A6F9', // Set the arrow color to red
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
