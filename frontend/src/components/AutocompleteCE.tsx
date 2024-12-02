import * as React from 'react';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import List from './AutocompleteList';

interface Option {
  label: string;
  id: number;
}

export default function AutoCompleteCE({}) {
  const [selectedValue, setSelectedValue] = React.useState<Option | null>(null);

  return (
    <Autocomplete
      disablePortal
      options={List}
      value={selectedValue}
      onChange={(event, newValue) => setSelectedValue(newValue)} // Update selected value
      sx={{
        width: 300,
        height: 40,
        backgroundColor: 'white',
        borderRadius: 15,
        margin: 1,

        '& .MuiOutlinedInput-root': {
          '& fieldset': {
            borderColor: 'transparent', // Remove the default outline
            borderRadius: 8,
            height: 45,
          },
          '&:hover fieldset': {
            borderColor: 'transparent', // Remove the outline on hover
          },
          '&.Mui-focused fieldset': {
            borderColor: '#32A6F9', // Remove the outline when focused
            top: 3,
          },
          // Adjusting the position of the dropdown arrow
          '& .MuiAutocomplete-popupIndicator': {
            top: '50%', // Align the arrow vertically at the center
            transform: 'translateY(0%)', // Adjust vertical centering
          },
        },
      }}
      renderInput={(params) => (
        <TextField
          {...params}
          label={selectedValue ? '' : "Category Type"} // Remove label after selection
          sx={{
            marginTop: -1,
            '& .MuiInputLabel-root': {
              color: '#848484', // Use state for label color
              fontFamily: 'Inter',
              //transform: 'translate(px, px)', // Move label up when selected
            },
            '& .MuiInputBase-input': { fontFamily: 'Inter' }, // Set input text font family to Inter
          }}
          InputLabelProps={{
            shrink: false,  // Ensure label stays consistent
          }}
        />
      )}
    />
  );
}
