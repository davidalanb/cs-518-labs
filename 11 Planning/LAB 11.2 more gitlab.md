## Gitlab etc

Scenario:

* We have created our project charter and initialized our Gitlab projects and repositories.
* Now, we will identify roles and responsibilities and setup the initial project codebase.
* After this, we can proceed to sprint planning.

## Identify team lead(s)

* Identify the team member(s) who will:
    - Contribute initial code
        * strong development skills, good testing practices, clean code, etc.
        * this person might act as a "lead developer," or "integrator" who has a good overall understanding of the project and code.
    - Be a maintainer - 
        * comfortable working with Git and Gitlab.
        * We will elevate this persons permission so they can modify project settings and/or push to main if necessary.

## Adding a starting codebase

* Add your starting project codebase to your local development folder.
    - you can decide what to take or leave from your coursework.
* Recommended structure:
    * group-project/
        - user-api/     <-- if you're using the user REST API        
        - other-api/    <-- if you're developing another REST API
        - app/          <-- your flask app
        - docs/         <-- documentation

## Development

### Keeping your dev branch updated

* Make sure your local main is up to date:
```
git checkout main
git pull
```
* Now switch to your dev branch and merge main into it.
```
git checkout <dev-branch>
git merge main
```

### Merge conflicts

* You might encounter merge conflicts when you merge new code into your dev branch.
* You should resolve these locally before pushing your dev branch and creating a merge request.

### Creating a merge conflict

* To get some practice, you have some options:
    - You can a teammate create separate branches and both make modifications to the same file.  Your teammate can merge to main first, and then try updating your branch with the changes to trigger a conflict.
    - Or, you can do the same thing yourself with two branches.

* TODO: team members should work together to create and resolve merge conflicts.