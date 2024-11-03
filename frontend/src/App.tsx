import { Routes, Route } from 'react-router-dom';
import { ThemeProvider } from '@mui/material/styles';
import theme from './theme';

import LandingPage from './pages/LandingPage';
import TodayPage from './pages/TodayPage';
import YesterdayPage from './pages/YesterdayPage';
import HistoryPage from './pages/HistoryPage';
import InsightsPage from './pages/InsightsPage';


import DBport from './pages/DBport';
import GoogleAPI from './pages/GoogleAPI';


function App() {
  return (
    <div className="bg-custombg min-h-screen">
    <ThemeProvider theme={theme}>
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/today" element={<TodayPage />} />
          <Route path="/yesterday" element={<YesterdayPage />} />
          <Route path="/history" element={<HistoryPage />} />
          <Route path="/insights" element={<InsightsPage />} />

          <Route path="/DBport" element={<DBport />} />
          <Route path="/google-api" element={<GoogleAPI />} />
        </Routes>

    </ThemeProvider>
    </div>
  );
}

export default App;