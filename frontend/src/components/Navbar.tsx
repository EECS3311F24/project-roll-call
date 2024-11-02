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
import { Link, useLocation } from 'react-router-dom';

const pages = [
  { label: 'Today', path: '/today' },
  { label: 'Yesterday', path: '/yesterday' },
  { label: 'History', path: '/history' },
  { label: 'Insights', path: '/insights' },
];

const settings = ['Profile', 'Account', 'Dashboard', 'Logout'];

function ResponsiveAppBar() {
  const location = useLocation();

  const [anchorElUser, setAnchorElUser] = React.useState<null | HTMLElement>(null);

  const handleOpenUserMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorElUser(event.currentTarget);
  };

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };

  return (
    <AppBar position="static" sx={{ backgroundColor: '#D9E5D6' }}>
      <Container maxWidth={false}>
        <Toolbar disableGutters sx={{ justifyContent: 'space-between', px: 1}}>
          
          {/* Logo on the Far Left */}
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

          {/* Page Navigation Buttons in the Center */}
          <Box sx={{ flexGrow: 1, display: 'flex', justifyContent: 'center', mr: 21}}>
            {pages.map((page) => (
              <Button
                key={page.label}
                component={Link}
                to={page.path}
                sx={{ 
                    my: 2, 
                    mx: 2,
                    color: 'black', 
                    display: 'block', 
                    textTransform: 'none',
                    fontSize: '1.0rem',
                    top: '4px',
                    fontWeight: location.pathname === page.path ? 'bold' : 'normal',
                }}
              >
                {page.label}
              </Button>
            ))}
          </Box>

          {/* User Avatar and Settings Menu on the Far Right */}
          <Box sx={{ flexGrow: 0 }}>
            <Tooltip title="Open settings">
              <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
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
