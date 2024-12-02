import { styled } from '@mui/material/styles';
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Switch from '@mui/material/Switch';
import '../DashboardPage.css';
import { SwitchCPProps } from '../types';

const SwitchCP = styled(Switch)(({  }) => ({
  width: 200,
  height: 48,
  padding: 7,

  '& .MuiSwitch-switchBase': {
    margin: 8,
    padding: 0,
    transform: 'translateX(-1px)',
    top: '-0.5px',

    '&.Mui-checked': {
      color: '#fff',
      transform: 'translateX(84px)',

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
      left: '30px',
    },
    '&::after': {
      content: "'Priority'",
      fontWeight: '700',
      fontSize: '12px',
      color: '#656C79',
      position: 'absolute',
      right: '30px',
    },
  },
}));

const CustomizedSwitches = ({ organize_by, toggleOrganize }: SwitchCPProps) => {
  return (
    <>
      <FormGroup>
          <FormControlLabel
            control={<SwitchCP sx={{ m: 1 }} checked={organize_by === 'priority'} onChange={toggleOrganize} />}
            label=""
          />
      </FormGroup>
    </>
  );
};

export default CustomizedSwitches;
