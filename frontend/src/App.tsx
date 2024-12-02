import { Routes, Route } from 'react-router-dom';
import ProtectedRoute from './components/ProtectedRoutes';

import { ThemeProvider } from '@mui/material/styles';
import theme from './theme';
import './index.css';

import DashboardPage from './pages/DashboardPage';
import LandingPage from './pages/LandingPage';
import TodayPage from './pages/TodayPage';
import NotFoundPage from './pages/NotFoundPage'; 
import YesterdayPage from './pages/YesterdayPage';
import HistoryPage from './pages/HistoryPage';
import InsightsPage from './pages/InsightsPage';

import TestPage from './pages/TestPage';



// our main a function which has our page routes
function App() {
  return (
    <div className="h-screen bg-custombg">
    <ThemeProvider theme={theme}>
        <Routes>
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
                <DashboardPage />
              </ProtectedRoute>
            }
          />  

          {/* 404 Page */}
         <Route path="*" element={<NotFoundPage />} />


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