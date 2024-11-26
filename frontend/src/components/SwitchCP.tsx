import * as React from 'react';
import { styled } from '@mui/material/styles';
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Switch, { SwitchProps } from '@mui/material/Switch';
import '../DashboardPage.css';

const SwitchCP = styled(Switch)(({ theme }) => ({
  width: 200,
  height: 48,
  padding: 7,

  '& .MuiSwitch-switchBase': {
    margin: 8,
    padding: 0,
    transform: 'translateX(-1px)',

    '&.Mui-checked': {
      color: '#fff',
      transform: 'translateX(85px)',

      '& .MuiSwitch-thumb:before': {
        content: "'Priority'",
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
        content: "'Priority'",
        fontWeight: '700',
        fontSize: '12px',
        backgroundColor: '#BFCDE5',
      },
    },
  },

  //Properties: for Thumb
  '& .MuiSwitch-thumb': {
    backgroundColor: '#32A6F9',
    width: 100,
    height: 32,
    borderRadius: 45,
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    textAlign: 'center',
    fontSize: '12px', // Adjust font size to fit "Category" inside
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
      content: "'Category'",
    },
  },

  //Properties: Track for Priority option
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

    // Add labels "Category" and "Priority" inside the track
    '&::before': {
      content: "'Category'",
      fontWeight: '700',
      fontSize: '12px',
      color: '#656C79',
      position: 'absolute',
      left: '23px',
    },
    '&::after': {
      content: "'Priority'",
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
                 control={<SwitchCP sx={{ m: 1 }} defaultChecked />}
                 label=""
               />
            </FormGroup>
        </>
  );
}
