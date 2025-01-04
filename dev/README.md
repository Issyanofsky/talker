# <p align="center">**Development**</p>


This folder is the develop side of the process.
on this folder are all the script are pushed.
-  api (folder) - contain the scrops for the Flask api.
-  htmlfile (folder) - containing the html files to be deployed.

on pushing a new content, it start a CI process [Git Action Workflow](/.github/workflows/) which test the new pushed script and if suceess
it will push it to production automaticaly.

testing:
- API (Flask) pipeline - a complete test and deploy (if success) to Docker Hub a new image. the test that are done are as follow:
    - checks that the HTTP response code is 200.
    - checks if the response data (the body of the response) matches the expected string (eg."Welcome to the add_event API!").
    - ensures that the Python code follows proper style guidelines (PEP 8).
    * important: the name of the API cant be changed (the python script)!!.
    if the test pass successfully it wrap the script in an image and push it into the docker repository (you have to create secret
    DOCKER_USERNAME, DOCKER_PASSWORD for DockerHub). the push is done only after a test done to ensure the image works correctly.

- HTML test - 
