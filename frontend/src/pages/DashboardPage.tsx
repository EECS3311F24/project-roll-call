import '../DashboardPage.css';
import Navbar from '../components/Navbar';
import SwitchWQ from '../components/SwitchWQ';
import SwitchCP from '../components/SwitchCP';
import SwitchYesNo from '../components/SwitchYesNo';
import SliderFG from '../components/SliderFG';
import TimeBubble from '../components/TimeBubble';
import AutoCompleteCE from '../components/AutocompleteCE';
import AutoCompletePrio from '../components/AutocompletePrio';
import { useState, useEffect } from 'react';
import axios from 'axios';
import { EventSettings, Settings} from '../types';

const isEventSettings = (obj: any): obj is EventSettings => {
  return obj && typeof obj.category === 'string' && typeof obj.color === 'number' || typeof obj.color === 'string';
};

const DashboardPage = () => {
  const [settings, setSettings] = useState<Settings | null>(null);
  const [greeting, setGreeting] = useState<string>('');
  const [organize_by, setOrganize] = useState<string>('');
  const [notification, setNotification] = useState<boolean>(true);

  useEffect(() => {
    const fetchSettings = async () => {
      try {
        const response = await axios.get('http://localhost:5000/setting/get_settings', {withCredentials: true});
        console.log(response.data);
        setSettings(response.data);
        setGreeting(response.data.greeting || 'word');
        setOrganize(response.data.organize_by || 'category');
        setNotification(response.data.notification);
      } catch (err) {
        console.error("Error fetching settings", err);
      }
    };
    fetchSettings();
	}, []);
  
  const categories = [];
  if (settings) {
    for (let i = 1; i <= 11; i++) {
      const eventKey = `e${i}` as keyof Settings;
      const event = settings[eventKey]

      if (isEventSettings(event) && event.category) {
        categories.push(event.category);
      }
    }
    console.log(categories);
  }

  const priorities = [];
  if (settings) {
    for (let i = 1; i <= 11; i++) {
      const eventKey = `e${i}` as keyof Settings;
      const event = settings[eventKey]

      if (isEventSettings(event) && event.priority) {
        priorities.push(event.priority);
      }
    }
    console.log(priorities);
  }

  const toggleGreeting = async () => {
    const newGreeting = greeting === 'quote' ? 'word' : 'quote';
    setGreeting(newGreeting);

    try {
      await axios.post('http://localhost:5000/setting/update_nonevent_setting', 
        {
          setting_key: 'greeting',
          new_value: newGreeting,
        },
        { withCredentials: true }
      );
    } catch (err) {
      console.error("Error updating greeting setting", err);
    }
  };

  const toggleOrganize = async () => {
    const newOrganize = organize_by === 'priority' ? 'category' : 'priority';
    setOrganize(newOrganize);

    try {
      await axios.post('http://localhost:5000/setting/update_nonevent_setting', 
        {
          setting_key: 'organize_by',
          new_value: newOrganize,
        },
        { withCredentials: true }
      );
    } catch (err) {
      console.error("Error updating organize_by setting", err);
    }
  };

  const toggleNotification = async () => {
    const newNotification = notification === true ? false : true;
    setNotification(newNotification);

    try {
      console.log('Payload:', { setting_key: 'notification', new_value: newNotification });
      await axios.post('http://localhost:5000/setting/update_nonevent_setting', 
        {
          setting_key: 'notification',
          new_value: newNotification,
        },
        { withCredentials: true }
      );
    } catch (err) {
      console.error("Error updating notification setting", err);
    }
  };

  type SettingsKey = 'e1' | 'e2' | 'e3' | 'e4' | 'e5' | 'e6' | 'e7' | 'e8' | 'e9' | 'e10' | 'e11';
  
  const handleCategoryChange = async (key: SettingsKey, newValue: string) => {
    if (!settings) return;
    const updatedSettings = { ...settings, [key]: { ...settings[key], category: newValue } };
    setSettings(updatedSettings);
    try {
      await axios.post(
        'http://localhost:5000/setting/update_event_setting',
        { setting_key: key, field_key: 'category', new_value: newValue },
        { withCredentials: true }
      );
      console.log(`Category for ${key} updated to ${newValue}`);
    } catch (err) {
      console.error(`Error updating category for ${key}`, err);
    }

    const updatedCategories: string[] = [];
    for (let i = 1; i <= 11; i++) {
      const eventKey = `e${i}` as keyof Settings;
      const event = updatedSettings[eventKey];

      if (isEventSettings(event) && event.category) {
        updatedCategories.push(event.category);
      }
    }
  };

  const handlePriorityChange = async (key: SettingsKey, newValue: string) => {
    if (!settings) return;
    const updatedSettings = { ...settings, [key]: { ...settings[key], priority: newValue } };
    setSettings(updatedSettings);
    try {
      await axios.post(
        'http://localhost:5000/setting/update_event_setting',
        { setting_key: key, field_key: 'priority', new_value: newValue },
        { withCredentials: true }
      );
      console.log(`Priority for ${key} updated to ${newValue}`);
    } catch (err) {
      console.error(`Error updating priority for ${key}`, err);
    }

    const updatedPriorities: string[] = [];
    for (let i = 1; i <= 11; i++) {
      const eventKey = `e${i}` as keyof Settings;
      const event = settings[eventKey]

      if (isEventSettings(event) && event.priority) {
        updatedPriorities.push(event.priority);
      }
    }
  };

  return (
    <>
        <div className="flex flex-col min-w-[800px] bg-custombg">
            <Navbar />
            <div className="container">
                <div className="container-center">
                    
                     <div className="heading-text">
                        Sara's Dashboard 
                      </div>

                    <div className="columns">
                      <div className="left-column">
                        <div className="sub-heading-text ">
                          Customize your Greeting
                        </div > 

                        {settings ? (
                          <SwitchWQ greeting={greeting} toggleGreeting={toggleGreeting} />
                        ) : (
                          <div>Loading...</div>
                        )}
                        
                        <div className="sub-heading-text ">
                          Classify your Calendar Events
                        </div > 
                        <div className="color-category">
                          <div className="color-stack">
                            <div className="circle bg-[#D50000]"></div>
                            <div className="circle bg-[#E67C73]"></div>
                            <div className="circle bg-[#F4511E]"></div>
                            <div className="circle bg-[#F6BF26]"></div>
                            <div className="circle bg-[#33B679]"></div>
                            <div className="circle bg-[#0B8043]"></div>
                            <div className="circle bg-[#039BE5]"></div>
                            <div className="circle bg-[#3F51B5]"></div>
                            <div className="circle bg-[#7986CB]"></div>
                            <div className="circle bg-[#616161]"></div>
                            <div className="circle bg-[#9E69AF]"></div>
                          </div>

                          <div className="category">
                            <div className="sub-sub-heading-text ">
                              Category Type
                            </div >
                            {categories.map((category, index) => (                              
                              <AutoCompleteCE
                                key={index}
                                label={String(category || `Category for ${index}`)}
                                onSelectionChange={(newValue) =>
                                  handleCategoryChange(`e${index + 1}` as SettingsKey, newValue)
                                }
                              />                              
                            ))}
                          </div>

                          <div className="priority">
                            
                            <div className="sub-sub-heading-text ">
                              Priority
                            </div > 
                            {priorities.map((priority, index) => (                              
                              <AutoCompletePrio
                              key={index}
                              label={String(priority || `Priority for ${index}`)}
                              onSelectionChange={(newValue) =>
                                handlePriorityChange(`e${index + 1}` as SettingsKey, newValue)
                              }
                            />                             
                            ))}
                          </div>
                        </div>
                      </div>    
                                          
                      <div className="right-column">
                        
                    <div className="sub-heading-text ">
                      Customize your Future at a Glance
                    </div >
                    
                    <div className="sub-sub-heading-text ">
                      Time frame in Weeks
                    </div >
                        <div className="slider">
                          <SliderFG/>  
                        </div> 

                        {settings ? (
                          <SwitchCP organize_by={organize_by} toggleOrganize={toggleOrganize} />
                        ) : (
                          <div>Loading...</div>
                        )}
                        
                    <div className="sub-heading-text ">
                      Notification
                    </div >
                    
                    <div className="sub-sub-heading-text ">
                      Get your report emailed to you
                    </div >
                        {settings ? (
                          <SwitchYesNo notification={notification} toggleNotification={toggleNotification} />
                        ) : (
                          <div>Loading...</div>
                        )}
                        
                    <div className="sub-sub-heading-text ">
                      Set a time to receive your report
                    </div >   
                        </div>
                        <div className="time-bubble">
                          <TimeBubble />
                        </div>     
                      </div>
                    </div>
                </div>
            </div>
    </>  
    
  )
}

export default DashboardPage

