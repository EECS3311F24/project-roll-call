import React from 'react';
import SummaryBubble from '../components/SummaryBubble';
import HelloBubble from '../components/HelloBubble';
import TodayBubble from '../components/TodayBubble';
import WeekBubble from '../components/WeekBubble';
import FutureBubble from '../components/FutureBubble';
import Navbar from '../components/Navbar';
import TodoBubble from '../components/TodoBubble';

// this is the page which displays the all the user reports for the current day
// current implementation includes only welcome, today and week bubbles
// the other bubbles are place holders 
const TodayPage = () => {

  return (
    <>
      <div className="flex flex-col min-w-[800px] bg-custombg">
        <Navbar />

        <HelloBubble />
  
        <div className="flex-grow px-[100px] mb-10">
          {/* <HelloBubble /> */}
          <div
            className="grid gap-2"
            style={{
              gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
              maxHeight: 'calc(100vh - <Navbar height>)',
            }}
          >
            <TodayBubble />
            <WeekBubble />
            <FutureBubble />
            <TodoBubble />
          </div>
        </div>
      </div>
    </>
  );
};

export default TodayPage;

