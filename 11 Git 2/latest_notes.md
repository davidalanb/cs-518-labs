
* Checkout a new branch:
    * git checkout -b dev-david
* view branches: 
    * git branch
* set upstream:
    git push -u origin dev-david
* develop and push to dev-david
    - git add <dir>
    - git commit -m <msg>
    - git push

# Submit a merge / pull request (PR)

* Go

# Merge straight to main (no PR)

* merge with main
    - git checkout main
    - git pull origin main
    - git merge dev-david

        - fix conflicts

    - git push origin main

