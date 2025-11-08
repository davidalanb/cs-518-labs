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

## Reverting changes

Scenario:

* You've accidentally committed some changes on your local main.
* But you can't push those to the remote because it's protected.
* So you need to save those changes to your dev branch
* And then, revert those changes (or reset if needed)

## Saving your changes

* If you want to keep the changes that you made to main, you will need to merge them into your dev branch.

```
git checkout david-dev
git merge main
```

### Reverting a commit

Reverting:

* view the commit history
    - the most recent commit will be on top
```
git log
```
* revert (undo a commit)
    - the hash is the long sequence of letters and numbers
    - e.g.: d849595cbd528f5d1451b5ca5b81946889f54ed5
```
git revert <HASH>
```

## Reset local main 

* ...back to the last commit it had in common with the remote

```
git checkout main
git reset --hard origin/main
```

