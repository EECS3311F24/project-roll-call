import { styled } from '@mui/material/styles';
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Switch from '@mui/material/Switch';
import '../DashboardPage.css';
import { SwitchYesNoProps } from '../types';

const SwitchYesNo = styled(Switch)(({ }) => ({
  width: 100,
  height: 48,
  padding: 6,

  '& .MuiSwitch-switchBase': {
    margin: 8,
    padding: 0,
    transform: 'translateX(-1px)',
    top: '-1px',

    '&.Mui-checked': {
      color: '#fff',
      transform: 'translateX(39.5px)',

      '& .MuiSwitch-thumb:before': {
        content: "'No'",
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
        content: "'No'",
        fontWeight: '700',
        fontSize: '12px',
        backgroundColor: '#BFCDE5',
      },
    },
  },

  //Properties: for Thumb
  '& .MuiSwitch-thumb': {
    backgroundColor: '#32A6F9',
    width: 46,
    height: 34,
    borderRadius: 45,
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    textAlign: 'center',
    fontSize: '12px', // Adjust font size to fit "Yes" inside
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
      content: "'Yes'",
    },
  },

  //Properties: Track for No option
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

    // Add labels "Yes" and "No" inside the track
    '&::before': {
      content: "'Yes'",
      fontWeight: '700',
      fontSize: '12px',
      color: '#656C79',
      position: 'absolute',
      left: '23px',
    },
    '&::after': {
      content: "'No'",
      fontWeight: '700',
      fontSize: '12px',
      color: '#656C79',
      position: 'absolute',
      right: '23px',
    },
  },
}));


const CustomizedSwitches = ({ notification, toggleNotification }: SwitchYesNoProps) => {
  return (
    <>
      <FormGroup>
          <FormControlLabel
            control={<SwitchYesNo sx={{ m: 1 }} checked={notification === false} onChange={toggleNotification} />}
            label=""
          />
      </FormGroup>
    </>
  );
};

export default CustomizedSwitches;