import Box from '@mui/material/Box';
import Slider from '@mui/material/Slider';
import { SliderFGProps } from '../types';

const marks = [
  { value: 2, label: '2' },
  { value: 3, label: '' },
  { value: 4, label: '4' },
  { value: 5, label: '' },
  { value: 6, label: '6' },
  { value: 7, label: '' },
  { value: 8, label: '8' },
  { value: 9, label: '' },
  { value: 10, label: '10' },
  { value: 11, label: '' },
  { value: 12, label: '12' },
];

function valuetext(value: number) {
  return `${value}`;
}

export default function SliderFG({ value, onChange }: SliderFGProps) {
  return (
    <Box sx={{ width: 300 }}>
      <Slider
        aria-label="Future at a Glance"
        value={value}
        getAriaValueText={valuetext}
        valueLabelDisplay="auto"
        shiftStep={3}
        step={1}
        marks={marks}
        min={2}
        max={12}

        onChange={(_, newValue) => {
          if (typeof newValue === 'number') {
            onChange(newValue);
          }
        }}
        
        sx={{
          '&.MuiSlider-root': {
            color: '#32A6F9',            // Change the slider color
          },
          '& .MuiSlider-rail': {
            backgroundColor: '#A2BCC5', // Color of the unfilled trail
          },
          '& .MuiSlider-thumb': {
            backgroundColor: 'white',
            width: 14,
            height: 14,
          },
          '& .MuiSlider-valueLabel': {
            backgroundColor: '#32A6F9', // Bubble background color
            borderRadius: 1,
          },
          '& .MuiSlider-mark': {
            backgroundColor: '#A2BCC5', // Keep marks grey
            width: 1.1,                 // Width of the mark
            height: 5,                  // Height of the mark
            top: 28,                    // Move the marks down 
          },
          '& .MuiSlider-markLabel': {
            color: '#A2BCC5',           // Color of the mark labels
            fontSize: '9px',            // Font size of the labels
            top: 36,                    // Adjust label position for alignment
          },
        }}

      />
    </Box>
  );
}
