import { Routes, Route } from 'react-router-dom';
import ProtectedRoute from './components/ProtectedRoutes';

import { ThemeProvider } from '@mui/material/styles';
import theme from './theme';
import './index.css';

import LandingPage from './pages/LandingPage';
import TodayPage from './pages/TodayPage';
import YesterdayPage from './pages/YesterdayPage';
import HistoryPage from './pages/HistoryPage';
import InsightsPage from './pages/InsightsPage';

import Dashboard from './pages/Dashboard';
import TestPage from './pages/TestPage';



// our main a function which has our page routes
function App() {
  return (
    <div className="h-screen bg-custombg">
    <ThemeProvider theme={theme}>
        <Routes>
          {/* Public Routes */}
          <Route path="/" element={<LandingPage />} />

          {/* Protected Routes */}
          <Route
            path="/today"
            element={
              <ProtectedRoute>
                <TodayPage />
              </ProtectedRoute>
            }
          />

          <Route
            path="/dashboard"
            element={
              <ProtectedRoute>
                <Dashboard />
              </ProtectedRoute>
            }
          />  


          {/* <Route path="/today" element={<TodayPage />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/test" element={<TestPage />} />

          <Route path="/yesterday" element={<YesterdayPage />} />
          <Route path="/history" element={<HistoryPage />} />
          <Route path="/insights" element={<InsightsPage />} /> */}


        </Routes>

    </ThemeProvider>
    </div>
  );
}

export default App;