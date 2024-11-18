
# Stand Ups

## Stand Up 1 (Saturday 2024-11-09)
### What we did since the last meeting:
1. Finished Suggested To-Do list backend logic and connected to front-end. 
2. Moved some shared helper functions into parent class events.py.
3. Created the backend logic for the future at glance list. 
4. Also improved today's bubble positioning.
5. Both the above implementations were merged ticket 12 and 00 with main
6. Added handling of All Day events which have a date attribute instead of dateTime and displayed it on the frontend.
7. Explored the backend implemented in sprint 1 for google authentication connection. 
8. Came across the client type under OAuth Client IDs in API’s and Services from google cloud is specified as-Desktop. Therefore created a separate Client ID with client type-Web Application to experiment with the implementation in order not to mess up the original backend calendar API.

### What we will commit to next:
1. Need to work on refining the front-end
2. Adding check boxes
3. Grey out completed tasks.
4. I will work on the frontend display of the future at glance bubbles.
5. Will work on implementation of word and quote generation via Google Gemini API.
6. Will work on implementation of Google OAuth Authentication via the new Client Type.

### When will we be done these:  
This will be done Nov 12 by the end of the day

### Any roadblocks along the way:
1. Had some trouble making the today page bubbles display in the way that we wanted, it required quite a bit of debugging as the divs were behaving unexpectedly.
2. Client type was causing errors and implementation issues.


## Stand Up 2 (Tuesday 2024-11-12)
### What we did since the last meeting:
1. Connected the future at a glance to the frontend.
2. Organized events to be displayed by event type.
3. Added a custom scroll bar. 
4. Merged ticket 14 to main.
5. Created Generator, QuoteGen, and WordGen classes to handle generating of quotes and word/definition.
6. Implemented google authentication through react and made a GoogleAuth.tsx component with using typescript on both client and server side.

### What we will commit to next:
1. Apply the same scroll bar customization to Today and week bubbles on today page.
2. Will work on displaying them on the frontend. 
3. Also will work on moving some functionality done on the frontend to the backend, as only information that’s needed should be returned to the frontend.
4.Fix the implementation to connect the LandingPage and Today page via the authentication.

### When will we be done these:
November 16th

### Any roadblocks along the way:
1. Some responses by the model were being repeated; ended up using randomized characters in the prompts to make it more likely to get unique responses.
2. Creation of a separate client ID and having two of them working on the same backend might be creating complications and this issue further needs to be investigated and resolved.


## Stand Up 3 (Saturday 2024-11-16)
### What we did since the last meeting:
1. Cleaned up code.
2. Custom scroll bars have been applied to today and week bubbles. 
3. Took a look at branch 17-- implementation of connecting the landing page with the today page. Noticed we were using the wrong Google OAuth client (desktop instead of Web App). Branch 17-- was using the correct one for the user authentication but our google calendar calls were using the wrong one. 
4. Restructured the app to be unified with a single OAuth client on another branch 17.1-- and changed it to Web Application. This made connecting to the landing page seamless, which we were able to complete!
5. Transferred/translated functionality from frontend to backend, returning only what’s needed to the frontend (TodayBubble, FutureBubble, WeekBubble). 
6. Added display of generated quote and word to the frontend.


### What we will commit to next: 
1. Next sprint we will move on to user account and customization.
2. Demo recording.
3. Note taking for the Sprint 1 Retrospective Meeting.
4. Summarize and push SR1.md to main.
5. System Design Document.
6. Standups.md.
7. Connect to the new login page and functionality.


### When will we be done these:
1. Sunday night Nov 17th (before deadline).
2. For sprint 3: Timeline and task will be more clear after our sprint 3 meeting


### Any roadblocks along the way: 
1. Building our app on the wrong google OAuth client was somewhat of a setback and required significant reconstruing and debugging that was not in our original plan
2. A lot was overhauled in terms of user login to the site, so will have to go through things to make it a seamless process with what we had before.
