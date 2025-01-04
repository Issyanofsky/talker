# <p align="center">**Talker**</p>


This folder is the develop side of the process.
on this folder are all the script are pushed.
-  api (folder) - contain the scrops for the Flask api.
-  htmlfile (folder) - containing the html files to be deployed.

on pushing a new content, it start a CI process [Git Action Workflow](/.github/workflows/) which test the new pushed script and if suceess
it will push it to production automaticaly.

testing:
- API (Flask) test - are done by a python script in the test folder that check the API by
    - checks that the HTTP response code is 200.
    - checks if the response data (the body of the response) matches the expected string (eg."Welcome to the add_event API!").
    - ensures that your Python code follows proper style guidelines (PEP 8) .

- HTML test - 
