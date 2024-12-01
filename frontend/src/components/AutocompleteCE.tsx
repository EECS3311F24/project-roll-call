import * as React from 'react';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import List from './AutocompleteList';

export default function ComboBox() {
  return (
    <Autocomplete
      disablePortal
      options={List}
      sx={{ width: 300, backgroundColor: 'white', borderRadius: 1 }} // Set white background
      renderInput={(params) => (
        
        <TextField 
          {...params} 
          label="Category Type"
          sx={{
            '& .MuiInputLabel-root': { color: 'black', fontFamily: 'Inter' }, // Set label color to black and font family to Inter
            '& .MuiInputBase-input': { fontFamily: 'Inter' } // Set input text font family to Inter
          }}
        />

      )}
    />
  );
}
