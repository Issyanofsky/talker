# <p align="center">**Talker**</p>

CRM app. this app is a small CRM for text speach loging. it record the speech and tag them by phone number. the app is based on HTML that serve as the fronthand. it
hosted on nginx servers. on the backend side there are api (Flask) that serve the app and also postgressSQL sever for the data (data saves on an nfs server outside the pods).
it publish outword (internet) by ingress as a Loadbalancer.
it implements a all CI/CD process (Continuous Deployment). the process start by pushing to the git repository any change done on the html's files (dev/htmlfiles)
or any change made on the python script (dev/api...) will be trigger the start of the CI/CD pipline that will end by deploying on the production side.

### folder content:
    
* dev folder - has the developer scripts.
* prod folder - this is the production folder. the folder contain the deployment of the application and the CD process. for more details [prod README.md](prod/README.md).
*
*   helm for deploying the app on the production side (k8s).deploy the "Talker" app. for more details [prod README.md](prod/README.md).
  the CD process is a  Continuous Deployment. it trigger by new image pushed to dockerhub (tag latest) and deploy it automaticaly into the production for the
  Flask api. and for the html (hosted on nginx) it triger by pushing new files into github repository (/prod/nginxhtml).
