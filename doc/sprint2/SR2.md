# Sprint 2 retrospective meeting

### Attendees: 
Karolina Tchilinguirova, Abhinaya Kondi, Christie Tang, Joshua Huliganga 

## Finished/Unfinished Tasks

All four of our user stores were completed in full:


    [5 story pts] As Alex (manager), I want to be displayed a motivational quote because my job is high stress and it will remind me to stay focused and be a good leader. And I want a word of the day because it is a fun feature which will motivate me to check RollCall every day.

    [9.0 story pts] As Sara(student), I want a “Suggested TODO list” that automatically generates based on my scheduled events, helping me prioritize my tasks for the day.

    [2.0 story pts] As Sara(student), I like to be able to check off items from my TODO list because it satisfying and motivating.

    [8.5 story pts]As Rachel(parent), I want a “Future at a glance” feature that highlights my further reaching events because my children have appointments which are planned weeks in advance and they always sneak up on me.

However, we had an additional task that was partially implemented. The task associated with ticket number 17 was not completed fully, thus was not able to be merged with main. 

    17--routing landing page


This task was more complicated than we initially anticipated. Therefore, this feature was demoed on a separate branch from the rest of the features. 

This task was thought to be a simple feature where we route the user from the landing page to the /today page while also prompting them to gain access to their Google Calendar. 

However, we ran into many bugs in the process, which led us to realize we needed to use a different type of Google authentication client. We used a desktop client when we should have used a Web Application client. We noticed this was why we could not automatically route the user back to the application after authentication. The desktop client does not provide the authentication redirection capabilities required for a web application. Therefore, we had to reconstruct the foundation of our app.py. 

We successfully implemented this new client but ran into merging issues that we could not solve by the end of this sprint. However, this was not a key feature in this sprint, and authentication + account management will be the focus of sprint 3. 

## Practices that should continue during next sprint
- Good team communication on discord
    - We were all engaged and present on discord and in team meetings. 
    - Responsive and engaged members
    - All members responded with 24 hours and no team mates ghosted

- Asking for help and providing it when needed.
- Good use of the trello

## Practices that NOT should continue during next sprint
- Not sticking to the designated git naming rules


## Harmful practices you should stop using during next sprint
- Non consistent nomenclature for git commits
- Moving forward we should stick to git commit messages being structured as 
    - "ticket number -- description" 
    - "00 -- description" for minor or unrelated commits

## Sprint Highs
- Seeing and demoing our prototype at the end of the sprint
- Scrum is a rewarding management process

## Sprint Lows
- Merging code conflicts is challenging and merging tools are confusing to learn
- Having to switch Google Authentication clients and restructuring our app.py
- Documentation is boring
