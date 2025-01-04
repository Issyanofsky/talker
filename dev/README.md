# <p align="center">**Talker**</p>


This folder is the develop side of the process.
on this folder are all the script are pushed.
-  api (folder) - contain the scrops for the Flask api.
-  htmlfile (folder) - containing the html files to be deployed.

on pushing a new content, it start a CI process [Git Action Workflow](/.github/workflows/) which test the new pushed script and if suceess it will push it to production automaticaly.

testing:
- API (Flask) test - are done by a python script in the test folder that check response from the API ( return staus code 200 and response from the root API http://localhost:port).
- HTML test - 
