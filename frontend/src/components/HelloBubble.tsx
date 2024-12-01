import { useEffect, useState } from 'react';
import axios from 'axios';

// Component which displays the welcome message on the today page. It includes a greeting, the date and word of the day
const HelloBubble = () => {
    const [wordData, setWordData] = useState({ word: '', definition: ''});
    const [quote, setQuote] = useState('');
    const [name, setName] = useState('');
	const [greeting, setGreeting] = useState('');

	useEffect(() => {
		const fetchSettings = async () => {
			try {
				const settingsResponse = await axios.get('http://localhost:5000/setting/get_settings', {withCredentials: true});
				console.log(settingsResponse.data);
				setGreeting(settingsResponse.data.greeting);
			} catch (err) {
				console.error("Error fetching settings", err);
			}
		};
		fetchSettings();
	}, []);

	useEffect(() => {
		if (greeting === 'word') {
		const fetchWord = async () => {
			try {
			const response = await axios.get("http://localhost:5000/gem/generate_word", {withCredentials: true});
			console.log(response.data);
			setWordData(response.data);
			} catch (err) {
			console.error("Error fetching word", err);
			}
		};
		fetchWord();
		} else if (greeting === 'quote') {
		const fetchQuote = async () => {
			try {
			const response = await axios.get("http://localhost:5000/gem/generate_quote", {withCredentials: true});
			console.log(response.data);
			setQuote(response.data);
			} catch (err) {
			console.error("Error fetching quote", err);
			}
		};
		fetchQuote();
		}
	}, [greeting]);

    useEffect(() => {
      const fetchName = async () => {
        try {
          const response = await fetch('http://localhost:5000/user/name', {
            method: "GET",
            credentials: "include",
          });
    
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
    
          const data = await response.json(); // Parse the JSON data
          setName(data); // Assuming the name is directly in the response object
        } catch (err) {
          console.error('Error fetching name:', err);
        }
      };

      fetchName();
    }, []);

    function greeting_name() {
      const currentHour = new Date().getHours(); // Get the current hour (0-23)
      let greeting;
    
      if (currentHour < 12) {
        greeting = `Good morning, ${name}!`;
      } else if (currentHour >= 12 && currentHour < 16) {
        greeting = `Good afternoon, ${name}!`;
      } else {
        greeting = `Good evening, ${name}!`;
      }
    
      return greeting;
    }
	
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
		<div className="bg-orange border rounded-[30px] mx-[200px] my-10 flex items-center justify-center transition-transform duration-300 transform hover:scale-105">

			<div className="flex-[40%] pl-7 px-4 py-6">
              <div className="text-2xl font-bold pb-1">{greeting_name()}</div>
              <div className="text-base">{todayDate()}</div>
          	</div>

			<div className="flex-[60%] pr-7 px-4 py-6 text-right">
					{greeting === 'word' ? (
						<>
						<div className="font-bold">
							Word: <span className="font-extrabold">{wordData.word}</span>
						</div>
						<div>{wordData.definition}</div>
						</>
					) : greeting === 'quote' ? (
						<>
						<div className="font-bold">
							Quote:
						</div>
						<div>{quote}</div>
						</>
					) : (
						<div>Loading...</div>
					)}           
			</div>

		</div>
	)
}

export default HelloBubble