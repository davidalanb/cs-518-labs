## Roles / Permissions

* Maintainer - 
    * can manage and push to protected branches (e.g., main)
* Developer - 
    * needs to create a merge request (a.k.a., pull request or PR)

## Setup

### Maintainer

* Create project in Gitlab
<!-- * create a branch for the new feature (e.g. features/basic) [optional for now - you can just use main] -->
* Enable Merge Requests
    - Settings > General > "Visibility, project features, permissions" > "Merge Requests" (enable)

### All

* clone project
```
git clone <url>
```
* create a branch for your personal work (e.g., dev-david)
    * your command should not include the '<' and '>' symbols
```
git checkout -b <name-of-branch>
```

## Developing on your personal branch

* Work on your code as normal.
* Periodically issue the commands:
    * git add - stage your new / modified files
    * git commit - commit to your local repo
    * git push - push to the remote (Gitlab)
* example below
    * note the '.' after add
```
git add .  
git commit -m "my commit message"  
git push
```

## Merging your personal branch with main

* In the response to the git push, GitLab provides a direct link to create the merge request.
* Go to the page provided in the link that was provided by Git and create your merge request. 
    * The merge request’s Source branch is your dev branch and the Target branch should be the main branch.
    <!-- * [If you are using a feature branch, that will be the Target.] -->
* If necessary, have your merge request reviewed.
    * Have someone merge your merge request, or merge the merge request yourself, depending on your process.

## Resolving merge conflicts

* When you create a merge request, there may be conflicts.
* If there are conflicts, you’ll see a warning like:
    * “This branch has conflicts that must be resolved before it can be merged.”
* You (or someone else) must resolve them.
* To do this:
    * checkout the source (if it isn't already checked out)
    * pull the target
    * resolve the conflicts
    * push changes to the dev branch
    * complete the merge request

* E.g., we created a PR to merge dev-david into main, but there are conflicts.
```
git checkout -b dev-david
git pull origin main
# resolve conflicts here
```
* After resolving conflicts, we push the changes to our dev branch.
```
git add .
git commit
git push
```
* now we should be able to complete the merge into main.

## Staying in sync

* To avoid conflicts, regularly pull main into your dev branch.
```
git pull origin main
```

## References

* https://docs.gitlab.com/user/permissions/ 
* https://docs.gitlab.com/topics/git/basics/ 
* https://docs.gitlab.com/topics/git/merge/ 
