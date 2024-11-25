import { Routes, Route } from 'react-router-dom';
import { ThemeProvider } from '@mui/material/styles';
import theme from './theme';
import './index.css';

import DashboardPage from './pages/DashboardPage';
import LandingPage from './pages/LandingPage';
import TodayPage from './pages/TodayPage';
import YesterdayPage from './pages/YesterdayPage';
import HistoryPage from './pages/HistoryPage';
import InsightsPage from './pages/InsightsPage';


import DBport from './pages/DBport';

// our main a function which has our page routes
function App() {
  return (
    <div className="h-screen bg-custombg">
    <ThemeProvider theme={theme}>
        <Routes>
          <Route path="/dashboard" element={<DashboardPage/>} />
          <Route path="/" element={<LandingPage />} />
          <Route path="/today" element={<TodayPage />} />
          <Route path="/yesterday" element={<YesterdayPage />} />
          <Route path="/history" element={<HistoryPage />} />
          <Route path="/insights" element={<InsightsPage />} />

          <Route path="/DBport" element={<DBport />} />
        </Routes>

    </ThemeProvider>
    </div>
  );
}

export default App;