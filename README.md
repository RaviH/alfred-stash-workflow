# alfred-stash-workflow
Workflow for Stash related actions.

Currently supported actions are:
* Stash setup: Needed to setup username, password and base url for Stash.
* Create Stash Project Repo Cache: Downloads and stores all the project repo combincation in a local file: stash.cache.
* Open Stash repository: Provides a list of stash reposiotories based on the stash cache created in the previous step.
* Open PRs created by you: lists all the PRs created by you.
* Open PRs for review by you: lists all the PRs open for your review.

###### Setup Base URL for Stash

1. Open Alfred (Opt + Spacebar)
2. Type stash setup baseUrl http://stash.com (Replace the url with your stash url)
3. Enter

![](http://i.giphy.com/BF3yKwKlT7DdC.gif)

###### Setup username for Stash

1. Open Alfred (Opt + Spacebar)
2. Type stash setup username your_username_here
3. Enter/Return

![](http://i.giphy.com/6R0dWmehY5hfy.gif)

###### Setup password for Stash

1. Open Alfred (Opt + Spacebar)
2. Type stash setup password your_password_here
3. Enter/Return

![](http://i.giphy.com/108ciS2VAZlT56.gif)

###### Setup Stash cache

1. Open Alfred (Opt + Spacebar)
2. Type stash create cache 
3. Enter/Return
4. This might take a minute or so. You will get a pop up once done.

###### Stash open repository list and select one repo to open

1. Open Alfred (Opt + Spacebar)
2. Type stash open repo 
3. Enter will open the selected repo in a browser.

Please let me know if their are any issues in using the workflow via creating an issue.
