import * as React from 'react';
import { styled } from '@mui/material/styles';
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Switch, { SwitchProps } from '@mui/material/Switch';


const SwitchWQ = styled(Switch)(({ theme }) => ({
  width: 140,
  height: 60,
  padding: 7,

  '& .MuiSwitch-switchBase': {
    margin: 8,
    padding: 0,
    transform: 'translateX(-1px)',

    '&.Mui-checked': {
      color: '#fff',
      transform: 'translateX(54px)',

      '& .MuiSwitch-thumb:before': {
        content: "'Quote'",
        fontSize: '12px', // Adjust font size to fit inside the circle
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        textAlign: 'center',
      },

      '& + .MuiSwitch-track': {
        opacity: 1,
        content: "'Quote'",
        fontSize: '12px',
        backgroundColor: '#BFCDE5',
      },
    },
  },

  //Properties: for Thumb
  '& .MuiSwitch-thumb': {
    backgroundColor: '#32A6F9',
    width: 70,
    height: 44,
    borderRadius: 45,
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    textAlign: 'center',
    fontSize: '12px', // Adjust font size to fit "Word" inside
    color: '#fff', // Ensure text is visible

    '&::before': {
      position: 'absolute',
      width: '100%',
      height: '100%',
      left: 0,
      top: 0,
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      content: "'Word'",
    },
  },

  //Properties: Track for quote option
  '& .MuiSwitch-track': {
    opacity: 1,
    backgroundColor: '#BFCDE5',
    borderRadius: 45,
  },
}));


export default function CustomizedSwitches() {
  return (
    <FormGroup>
      <FormControlLabel
        control={<SwitchWQ sx={{ m: 1 }} defaultChecked />}
        label=""
      />
    </FormGroup>
  );
}
