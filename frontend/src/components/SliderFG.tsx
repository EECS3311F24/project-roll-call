import * as React from 'react';
import Box from '@mui/material/Box';
import Slider from '@mui/material/Slider';

function valuetext(value: number) {
  return `${value}°C`;
}

export default function SliderFG() {
  return (
    <Box sx={{ width: 300 }}>
      <Slider
        aria-label="Future at a Glance"
        defaultValue={3}
        getAriaValueText={valuetext}
        valueLabelDisplay="auto"
        shiftStep={3}
        step={1}
        marks
        min={1}
        max={11}
      />
      <Slider defaultValue={3} step={1} marks min={1} max={11} disabled />
    </Box>
  );
}
