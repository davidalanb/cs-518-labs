## Working with git

Overview: 
* the team will collaboratively edit several files in your repo. 
* in doing so, they will probably encounter merge conflicts, which they will have to resolve.

### First team member creates directories / files 
 
* In the root of your working directory, add an "Intros" folder  
* In the "Intros" folder, create a text document \<your-name\>.txt with a brief self-introduction.  
* In a terminal, go to the root directory of your repo.  
* Stage, commit, and push your files (note the dot after add):  
```
git add .  
git commit -m "my first commit"  
git push
```

### Other members pull 

* Other team members, run this command to update your local repo:  
```
git pull
```
* Create your own intro file in the "Intros" folder, and then stage, commit, and push (like above).

### Modifying other files

* "Comment" on each of your teammates' documents by adding text to your local copies.  
  * pull 
  * edit the file
  * stage, commit, and push, just like above

### Merge conflicts

* If you and a teammate modify a file at the same time, one or both of you will encounter a merge conflict.  
* You will encounter a merge conflict on pull.
* to get more information about conflict(s):
```
git status
```
* open the file and you will see conflict markers, like this:
```
<<<<<<< HEAD
this is some content to mess with
content to append
=======
totally different content to merge later
>>>>>>> new_branch_to_merge_later
```
* Your changes are above the divider, and the conflicting changes are below the divider
* Determine which change to keep, or combine them in some way, and remove the conflict markers.