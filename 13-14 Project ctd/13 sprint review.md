## **\[20\] Sprint review**

* document:  
  * \[2\] review sprint goal and responsibilities (use 2x2 matrix)  
  * \[4\] review product backlog (by feature, then by developer)  
  * \[2\] next steps  
* etc:  
  * \[8\] **demo video (new features only)**  
  * \[4\] **Gitlab: updated issue board, sprint burndown chart**  
    * all team members commit code 

## Backlog review

Review the work items selected for the sprint.  Completed stories have unit and integration tests.  

For example:

### Adventure Discovery

|item|status|discussion
|---|---|---
|As an aspiring adventurer, I want to browse all adventures and see title and a brief description, so that I can get an idea of what's offered on the platform.|DONE|API endpoint done/tested; UI is mock tested; frontend is integrated with API
|As an aspiring adventurer, I want to view a list of adventures being offered by a specific guide|DONE|API endpoint done; UI done; integrated

### Adventure Creation

|item|status|discussion
|---|---|---
|As a guide, I want to specify a title and description for my adventure, so that..|DONE|
As a guide, I want to specify location, so that..|NOT DONE|API route is done; frontend is not done

## Demo

Demo by feature, then by developer (backend/frontend).  The demo should be very concise (~5-10 min).  Each individual should present their own work.

### feature X

Describe the feature being demoed / tested.

* Backend demo (demo internal or external API)
  - **Introduce yourself**
  - show testing script(s) and explain what is being tested
    - e.g. unittests that are executing your API functions (internal) OR calling your API endpoints (external)
  - run test(s) and show results
  
* frontend demo:
  - **Introduce yourself**
  - show testing script(s) and explain what is being tested
    - e.g. written instructions for a user to complete one or more stories, or (optionally) automated UI tests
  - demonstrate the feature (story or stories) by follow the instructions 