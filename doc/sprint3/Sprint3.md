# Sprint 3 Meeting

### Attendees: 
Karolina Tchilinguirova, Abhinaya Kondi, Christie Tang, Joshua Huliganga 

### Sprint Goal:
In this sprint we will focus on the account management and user customization. This sprint will consist of both backend and frontend development. 

By the end of this sprint we aim:
- implement a MonogoDB cloud database which will store:
    - user's credentials
    - user settings (preferred user customizations) 
- allow the user to sign Up, login and logout
- create a frontend interface for the user's dashboard (this is where the user will set their customizations preferences)
- allow for user customization; this will include:
    - allow the user to assign categories to their events by color or keyword
    - allow the user to assign priority to their events by color or keyword 
    - allow the user to assign customize their future at a glance summary by choosing:
        - length of time
        - categories to display
    - allow the user to enable the notification email and set the time
- update our hardcoded logic in future at a glance and suggested TODO to be dynamic based on user settings
- allow the user to share their report to others
- automatically email the users report to them (works as a notification)


### Stories to be completed (On Trello: Sprint 3 Backlog):

| Story Points (0-10 linear linear scale) | User Story                                                                                         |
|--------------|---------------------------------------------------------------------------------------------------|
| 10.0          | As Sara(student), I want the ability to customize my reports using personalized priority and lengths of time.  I like to be reminded of events far in the future if they are very important and want to customize my reports |
| 7.0          | As Alex(manager), I want to create an account and log in so that I can securely access my personalized settings and data |
| 6.0          | As Alex(manager), I want to be emailed my report (notification feature) because I already start my day with checking my inbox and having my report in my inbox saves me time + I do not need to remember to open RollCall. |
| 6.0          |As Sara(student), I want to be able to share my report with my partner because I am very busy and it is easier to plan time to spend together if my schedule is clearly outlined without me having to explain when I am available. |


### Team Capacity: 44 hours 

### Story decisions and task breakdown (On Trello: Sprint 2 Tasks):

| Team Members       | Activities/Tasks                                                                                        |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| **Karolina**      | - Note taker for Sprint 3 meeting and Sprint 3 Retrospective Meeting.<br> - Summarize and push `Sprint3.md`, `SR3.md` to main.<br> - Create user dashboard wireframe <br> - Implement sharing report feature <br> - Implement notification feature |
| **Abhinaya**      | - Summarize standup meetings and push `Standups.md` to main.<br> - Create the user dashboard frontend <br> - Implement user log out features |
| **Joshua**        | - Initialize the cloud db <br> - Create the login-api <br> - Crete the user setting-api <br>  |
|**Christie**      | - Reconstruct the event classes to be able to dynamically change logic based on user settings |
| **Group Effort**  | - Update documentation<br> - Record Demo - `burndown.pdf` - `schedule.pdf` -  `SYSTEM DESIGN DOCUMENT.pdf` |

