import * as React from 'react';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import List from './AutocompleteList';

export default function ComboBox() {
  return (
    <Autocomplete
      disablePortal
      options={List}
      sx={{ width: 300, backgroundColor: 'white', borderRadius: 1 , }} // Set white background
      renderInput={(params) => <TextField {...params} label="Category Type" />}
    />
  );
}
