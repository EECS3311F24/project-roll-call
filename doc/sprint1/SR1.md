# Sprint 1 retrospective meeting

### Attendees: 
Karolina Tchilinguirova, Abhinaya Kondi, Christie Tang, Joshua Huliganga 

## Unfinished Tasks
The following User Story was not completed this sprint:

    As Rachel(parent), I want a “Future at a glance” feature that highlights my further reaching events because my children have appointments which are planned weeks in advance and they always sneak up on me.

This task was more complicated then we initially anticipated, therefore it was not displayed in our sprint 1 prototype. 

It was more complicated because we realized we did not want to output a simple list of all events occurring in the "future," as this list would be too long and useless. Instead, we want to implement a logic which will sort these events based on priority and only output events of high priority occurring in the next month. 

We began implementing this feature and have completed the retrieval of the month events in *backend\flask_app\calendar_api\month_event.py*. However, we plan to add prioritization logic, which will be implemented in the upcoming sprints. 

## Practices that should continue during next sprint
- Good branch and pull/push communication
    - We were clear about what we were working on and minimized code conflicts   

- Appointing a leader allowed us to stay organized and make decision faster
- Responsive and engaged members
    - All members responded with 24 hours and no team mates ghosted

- Having the team leader create a meeting agenda kept meetings on track and efficient. 

## Practices that NOT should continue during next sprint
- Some group members took on too many tasks because they thought it would be quicker to do them themselves, then asking for help or assigning them to others.
- Too many tasks were assigned to all members which led to situations such as those mentioned above.


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
- Creating responsive web design is a challenge
- Documentation is boring
