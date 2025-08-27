### Outline

* Install tools
* Setup Git and Gitlab
* Create and clone individual project
  - this project will contain all of your individual work for the semester

### Tools and resources

Core tools:

* Python 3.11
* IDE / VSCode
* Git

Resources:

* [SSH Keys in Gitlab](https://gitlab.cs.unh.edu/help/user/ssh.md)
* [Git cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf)

### Creating SSH key

configure your username and email

* Open Git bash or your terminal of choice.  
* Use these commands:  

```
  git config --global user.name "John Doe"  
  git config --global user.email johndoe@example.com
```

Generate SSH keys:

* open Git bash or your terminal of choice. 
* input this command:   

```
ssh-keygen -t rsa -b 2048  
```

* you can just press enter at the prompts
* the public keys will be in a file ending in .pub

### Adding SSH keys to Gitlab

Add SSH keys to Gitlab

* [Log in to Gitlab](https://gitlab.cs.unh.edu/users/sign_in);   
* Go to User settings
* Go to SSH keys  
* Paste the entire contents of the .pub file from above

### Creating your project

Create a new project in Gitlab:

  - use the naming convention \<lastname\>-project 
  - do not include '<' and '>' symbols
  - e.g., benedetto-project

Add your grader with permissions >= "Reporter".

* In the left sidebar go to Manage -> Members
* Add your grader according to the table below

| Section | Students | Initials | Gitlab | Email |
| :--- | :--- | :--- | :--- | :--- |
| Sect 01 | Aleksas - Nimoji | AA | aa1667 | Alakbar Askarov <Alakbar.Askarov@unh.edu> |
| Sect 01 | Palermo - Subruto | DD | dcd1043 | Diego Dela Cruz <Diego.DelaCruz@unh.edu> |
| Sect 01 | Sullivan - Vecherin | JR | jiu8 | Jason Reeves <Jason.Reeves@unh.edu> |
| Sect 02 | Brady - Prout | MB | mmb1177 | Maeve Burwell <Maeve.Burwell@unh.edu> |
| Sect 02 | Saranich - Sullivan | DB | dabenedetto | David Benedetto <David.Benedetto@unh.edu> |

### Cloning your project

Cloning your project:

* get your clone link on Gitlab
  * Click the blue "Code" button on the home page for your project
  * then copy the link to your clipboard

![clone link](img/clone-link.png)

* create a directory for your CS 518 coursework (e.g. "/path/to/cs518").
* go to the directory in the terminal and clone the repo  

```
git clone <url>  
```

* replace \<url\> with the ssh clone link from Gitlab.
* after cloning, there will be a new folder (e.g., "path/to/cs518/my-project" )
* this is the root of your working directory for group work.

### Making your first commit

* Open your local working directory in VS Code.
* Modify README.md and/or create a new file
* Use the commands below to:
  * stage all files in your working directory (assuming you are running the command from the root directory)
  * commit the staged files to your local repo
  * push your changes to the remote (on gitlab.cs.unh.edu)

```
git add .
git commit -m "my first commit"
git push
```