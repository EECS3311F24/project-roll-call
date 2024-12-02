import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import List from './AutocompleteList';
import { AutoCompleteCEProps } from '../types';

export default function AutoCompleteCE({ label, onSelectionChange }: AutoCompleteCEProps) {
  return (
    <Autocomplete
      disablePortal
      options={List}
      sx={{
        width: 300,
        height:40,
        backgroundColor: 'white',
        borderRadius: 15,
        margin:1,

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
          },
           // Adjusting the position of the dropdown arrow
          '& .MuiAutocomplete-popupIndicator': {
            top: '50%', // Align the arrow vertically at the center
            transform: 'translateY(-30%)', // Adjust vertical centering
          },
        },
      }}

      onChange={(_, newValue) => {
        if (newValue) {
          const selectedValue = typeof newValue === 'object' && 'label' in newValue ? newValue.label : newValue;
          onSelectionChange(selectedValue);
        }
      }}

      renderInput={(params) => (
        <TextField 
          {...params} 
          label={label}
          sx={{
            '& .MuiInputLabel-root': { color: '#848484', fontFamily: 'Inter', transform: 'translate(14px, 8px)',}, // Set label color to black and font family to Inter
            '& .MuiInputBase-input': { fontFamily: 'Inter' }, // Set input text font family to Inter
          }}
        />
      )}
    />
  );
}
