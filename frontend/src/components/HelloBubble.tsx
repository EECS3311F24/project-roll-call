import React from 'react'

const HelloBubble = () => {

    const username = "Sara"

    const word = "Disbursement"
    const definition = "A disbursement is a payout of money from a fund that has been created for a special purpose. Disbursement can also refer to the money that is paid out."

    function todayDate() {
        const weekday = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
        const months = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"];
        const d = new Date();
    
        let day = weekday[d.getDay()];
        let month = months[d.getMonth()];
        let date = d.getDate();
        if (date === 1 || date === 21 || date === 31){
          return `Today is ${day}, ${month} ${date}st.`;
        }
        if (date === 2 || date === 22){
          return `Today is ${day}, ${month} ${date}nd.`;
        }
        if (date === 3 || date === 23){
          return `Today is ${day}, ${month} ${date}rd.`;
        } else {
          return `Today is ${day}, ${month} ${date}th.`;
        }
    }

    return (

      <div className="bg-orange border rounded-[30px] mx-[200px] my-10 flex h-full items-center justify-center transition-transform duration-300 transform hover:scale-105">
  
          <div className="flex-[40%] pl-7 px-4 py-6">
              <div className="text-2xl font-bold pb-1">Good Morning {username}!</div>
              <div className="text-base">{todayDate()}</div>
          </div>
  
  
  
          <div className="flex-[60%] pr-7 px-4 py-6 text-right">
              <div className="font-bold">
                  Word of the day: <span className="font-extrabold">{word}</span>
              </div>
              {definition}
          </div>
  
      </div>
    )
  }

export default HelloBubble
