import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';
import MenuItem from '@mui/material/MenuItem';
import Menu from '@mui/material/Menu';
import CalendarIcon from '@mui/icons-material/CalendarMonth';
import { Link, useLocation, Navigate } from 'react-router-dom';

// This is a navigation bar component which routes to different pages
const pages = [
  { label: 'Today', path: '/today' },
  { label: 'Yesterday', path: '/yesterday' },
  { label: 'History', path: '/history' },
  { label: 'Insights', path: '/insights' },
];

const settings = ['Profile', 'Account', 'Dashboard', 'Logout'];

function ResponsiveAppBar() {
  const location = useLocation()

  const [anchorElUser, setAnchorElUser] = React.useState<null | HTMLElement>(null);

  const handleOpenUserMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorElUser(event.currentTarget);
  };

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };

  if (location.pathname !== '/today') {
    return <Navigate to="/today" />;
  }
  

  return (
    <AppBar position="static" sx={{ backgroundColor: '#D9E5D6' }}>
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          
          {/* Logo */}
          <Link to="/" style={{ display: 'flex', alignItems: 'center', textDecoration: 'none', color: 'inherit' }}>
            <CalendarIcon sx={{ fontSize: 45, mr: 1, color: 'black' }} />
            <Typography
              variant="h6"
              noWrap
              sx={{
                fontWeight: 800,
                letterSpacing: '.1rem',
                color: 'black',
                textDecoration: 'none',
                fontSize: '1.8rem',
                position: 'relative',
                top: '4px',
              }}
            >
              Roll Call
            </Typography>
          </Link>

          {/* Page Navigation Buttons */}
          <Box sx={{ flexGrow: 1, display: 'flex' , ml: 7}}>
            {pages.map((page) => (
              <Button
                key={page.label}
                component={Link}
                to={page.path}
                sx={{ 
                    my: 2, 
                    ml: 5,
                    color: 'black', 
                    display: 'block', 
                    textTransform: 'none',
                    fontSize: '1.0rem',
                    top: '4px',
                    fontWeight: location.pathname === page.path ? 'bold' : 'normal',
                }}
                disabled={page.path !== '/today'} // Disable all buttons except "Today"
              >
                {page.label}
              </Button>
            ))}
          </Box>

          {/* User Avatar and Settings Menu */}
          <Box sx={{ flexGrow: 0 }}>
            <Tooltip title="Open settings">
              <IconButton onClick={handleOpenUserMenu} sx={{ p: 0, }}>
                <Avatar alt="User Avatar" src="/static/images/avatar/2.jpg" />
              </IconButton>
            </Tooltip>
            <Menu
              sx={{ mt: '45px' }}
              id="menu-appbar"
              anchorEl={anchorElUser}
              anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
              keepMounted
              transformOrigin={{ vertical: 'top', horizontal: 'right' }}
              open={Boolean(anchorElUser)}
              onClose={handleCloseUserMenu}
            >
              {settings.map((setting) => (
                <MenuItem key={setting} onClick={handleCloseUserMenu}>
                  <Typography sx={{ textAlign: 'center' }}>{setting}</Typography>
                </MenuItem>
              ))}
            </Menu>
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
}

export default ResponsiveAppBar;