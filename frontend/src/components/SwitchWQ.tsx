import * as React from 'react';
import { styled } from '@mui/material/styles';
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Switch, { SwitchProps } from '@mui/material/Switch';
import '../DashboardPage.css';

const SwitchWQ = styled(Switch)(({ theme }) => ({
  width: 150,
  height: 48,
  padding: 7,

  '& .MuiSwitch-switchBase': {
    margin: 8,
    padding: 0,
    transform: 'translateX(-1px)',

    '&.Mui-checked': {
      color: '#fff',
      transform: 'translateX(65px)',

      '& .MuiSwitch-thumb:before': {
        content: "'Quote'",
        fontSize: '12px', // Adjust font size to fit inside the circle
        fontWeight: '700',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        textAlign: 'center',
        color: '#fff',
      },

      '& + .MuiSwitch-track': {
        opacity: 1,
        content: "'Quote'",
        fontWeight: '700',
        fontSize: '12px',
        backgroundColor: '#BFCDE5',
      },
    },
  },

  //Properties: for Thumb
  '& .MuiSwitch-thumb': {
    backgroundColor: '#32A6F9',
    width: 70,
    height: 32,
    borderRadius: 45,
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    textAlign: 'center',
    fontSize: '12px', // Adjust font size to fit "Word" inside
    color: '#fff',

    '&::before': {
      position: 'absolute',
      width: '100%',
      height: '100%',
      left: 0,
      top: 0,
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      fontWeight: '700',
      content: "'Word'",
    },
  },

  //Properties: Track for quote option
  '& .MuiSwitch-track': {
    opacity: 1,
    backgroundColor: '#BFCDE5',
    borderRadius: 45,
    //--------------------------------------------------------------
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
    padding: '12px',
    boxSizing: 'border-box',

    // Add labels "Word" and "Quote" inside the track
    '&::before': {
      content: "'Word'",
      fontWeight: '700',
      fontSize: '12px',
      color: '#656C79',
      position: 'absolute',
      left: '23px',
    },
    '&::after': {
      content: "'Quote'",
      fontWeight: '700',
      fontSize: '12px',
      color: '#656C79',
      position: 'absolute',
      right: '23px',
    },
  },
}));


export default function CustomizedSwitches() {
  return (
    <>
            <FormGroup>
               <FormControlLabel
                 control={<SwitchWQ sx={{ m: 1 }} defaultChecked />}
                 label=""
               />
            </FormGroup>
        </>
  );
}
