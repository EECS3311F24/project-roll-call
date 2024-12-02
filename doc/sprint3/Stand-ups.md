# Stand Ups

## Stand Up 1 (Wednesday 2024-11-20)
### What we did since the last meeting:
1. Created a new Dashboard page connected under the Navigation bar. 
2. Created the center bubble for dashboard settings of the user. 
3. Got the basic layout of the toggle button specifically for the word and quote.

### What we will commit to next:
1. I will update and make the toggles similar to the ones decided in figma wireframes. 
2. Also once a single toggle is done getting the other three done should be easy.
3. Start to think about how to implement a notification feature + revisit account/token management

### When will we be done these:  
Wednesday 2024-11-27

### Any roadblocks along the way:
1. Figuring out how to come up with a basic toggle button that works smoothly took a considerable effort and exploration from my end.

## Stand Up 2 (Wednesday 2024-11-27)
### What we did since the last meeting:
1. Finished implementing the toggle buttons. 
2. The slider was comparatively easier to start with because of the familiarity. 
3. Got the time picker set up. Setup the color icons for each of the label. 
4. I have figured out how to automatically generate a user account when they authenticate through google. 
5. I have also been able to store user id in a Flask Sessions and the user's token in the database. 
6. Cleaned up the google calendar api call flow: fetch user id from session, use this to get a token, use token to make the api call.

### What we will commit to next:
1. I will fix the clock. 
2. Get the dropdowns implemented. 
3. I will implement the notification feature. 

### When will we be done these: 
Saturday 2024-11-30 

### Any roadblocks along the way:
1. The clock is complicated and throws the other components out of the frame so should get that fixed. 
2. When implementing the database, account and token management I noticed our backend organization was not very scalable and was starting to get bloated. 
3. Therefore, I organized the backend into 3 main folders: routes, services (business logic to serve the routes) and utilizes (any other methods)


## Stand Up 3 (Saturday 2024-11-30)
### What we did since the last meeting:
1. Implemented the drop-downs and also arranged them accordingly on the dashboard.
2. Fixed the drop-down overlapping issue and made the drop-down list for both Category-type and for Priority.
3. I have implemented a notification feature, which will automatically send users their roll call report at 9am in the morning.
4. I have also implemented a working share report button on the /today, which will open a dialog box and a user can send their report to a friend via email.


### What we will commit to next:
1. Finish the documentation and push standups.md. 
2. Finish recording the demo video. 
3. Get the other personas account for Alex created and to make their demo calendar that can be used with our app during the demo. 
4. I will update documentation, create another google calendar for another persona for Rachel, update the burndown, update the system design doc. 

### When will we be done these:  
Sunday 2024-12-01

### Any roadblocks along the way:
1. Making the page responsive with many components was challenging but ended up making it responsive only with-in the blue-container but not completely for the dashboard page. 
2. Also the overlapping was an issue for the drop down list. 
3. Implementing the automatic scheduler was quite challenging because currently we use a flask session with a user id stored in it to keep track of user credits required for Google api calls. 
4. However, a scheduler would be working out of session. Therefore, I had to change my approach and experiment with lots of different things before it got to work.

