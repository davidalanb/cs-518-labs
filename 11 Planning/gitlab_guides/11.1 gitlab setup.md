# Gitlab setup

## Outline

* Git (terminal)
    - clone repo
    - create dev branch
    - switch to dev
        - create file(s)
        - stage and commit
        - push to remote
* Gitlab (browser)
    - create MR
    - classmate approves
* Git (terminal)
    - switch to main
    - pull changes

* STUDENTS: Skip to "Working with your repo"

## [Instructors / TAs] Setup groups and projects

* Setup iterations in the supergroup (e.g., CS-518/fall-2025)
* create groups for teams (e.g. group-1A)
* add members as Developers
* create project
    - blank project
    - leave "Initialize repo..." checked
* configure merge requests
    - turn on merge requests
    - turn on merge request approvals (at least 1, not author)
* configure main branch
    - allow developers to merge
    - allow no one to push and merge

## [STUDENTS] Working with your repo

### Get your clone URL

* Go to the project
* Press the blue "Code" button
* Copy the URL for "clone with SSH"
    - you will use this below

### Add files to the repo

(Assumes repo has been initialized with a README)

* Open a terminal in the directory that will contain your project directory (e.g. CS-518/)
* Clone the project
    - this will create a new directory (e.g. CS-518/group-project/)
```
git clone <URL>
```
* create and switch to a branch called '<name>-test', e.g. 'david-test'
    * this will branch from main, since that's the branch you were on
```
git branch david-test
git checkout david-test
```
* Create a test file in group-project
* stage and commit
```
git add .
git commit -m 'david-test'
```
* push the code to the repo
```
git push origin david-test
```

### Creating and approving merge requests

Creating:

* Go to your project on Gitlab
* You should see a dialog at the top of the page with a blue button "Create merge request", click this.
    * You can also create MRs by going left-sidebar > Code > Merge requests.
* Give the MR an appropriate title
* Add yourself as an assignee and add a teammate as a reviewer
* Create the MR

Approving (you need to have another project member approve your MR):

* Go to Merge Requests in the left-sidebar
* Approve and merge

### Updating your local main

* in your terminal, switch back to the main branch and pull the latest code
```
git checkout main
git pull
```
