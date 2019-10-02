# GIT Guide

## A new repository

from an existing folder

`$ git init`

## Create a copy of the repository

from a server (usually GITHUB)

`$ git clone _url_`

or fork

## Adding to GITHUB

Create the repository in GITHUB first (safer)

`$ git remote add origin <URL>`

`$ git remote -v // Validates origin`

`$ git push origin master`

## Check status

`$ git status`

`$ git log --pretty=oneline`

`$ git diff // shows you changes that you have not tracked`

## Add your local changes to the STAGING area

`$ git add _filename_`

`$ git add .`

## COMMIT changes

`$ git commit -m "message"`

`$ git commit -am "Commit message" // adds and documents at the same time`

## Tags

In the following example use log to find the checksum.  They always point to the same commit.

`$ git tag -a <tag> -m _message_ <_part_checksum_>`

`$ git tag (to show tags)`

`$ git checkout tag (to load the code associated with the tag)`

## Branching

Allows various versions of the code at the same time.  Points to the last commit in the path

`$ git branch _name_`

`$ git checkout _name_`

`$ git merge _name_`

`$ git branch -d _name_`

## Merging changes

The editor will show HEAD>>c<<# where c is the conflict and #is the number of commit
You change the code and push it again.
For this is better to use a good editor not the commands

## Push to REMOTE repository

Identify yourself
 `$ git config –global user.name “[name]”`

Define remote name and push
```
$ git remote add origin https://github.com/cesell/modelproj.git
$ git push -u origin master  // it can be a branch instead of master
```


## Going to a previous version

`$ git reset --hard _commit_`
`$ git reset --hard origin/master`

## TIP: How to filter a file (maybe too big)

`$ git filter-branch --tree-filter 'rm -rf path/to/file' HEAD`

`$ git push`
