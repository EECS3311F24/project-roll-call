import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import List from './AutocompleteListPrio';
import { AutoCompletePrioProps } from '../types';

export default function AutoCompletePrio({ label, onSelectionChange }: AutoCompletePrioProps) {
// interface Option {
//   label: string;
//   id: number;
// }

// export default function AutoCompletePrio({}) {
//   const [selectedValue, setSelectedValue] = React.useState<Option | null>(null);

  return (
    <Autocomplete
      disablePortal
      options={List}
      // value={selectedValue}
      // onChange={(event, newValue) => setSelectedValue(newValue)} // Update selected value
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
          // label={selectedValue ? '' : "Priority"} // Remove label after selection
          sx={{
            marginTop: -1,
            '& .MuiInputLabel-root': {
              color: '#848484', // Use state for label color
              fontFamily: 'Inter',
              transform: 'translate(px, px)',
            },
            '& .MuiInputBase-input': { fontFamily: 'Inter' }, // Set input text font family to Inter
          }}
        />
      )}
    />
  );
}
