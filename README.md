# <p align="center">**Talker**</p>

CRM app. this app is a small CRM for recording speech and tag them by phone number.the app is based on HTML that serve as the fronthand hosted on nginx servers.
it use ingress as a Loadbalancer and postgresSQL as database. ALL data is stored out side the pods on a nfs file server.
it implements a all CI/CD process. from pushing any change done on the html's files (dev/htmlfiles) or any change made on the python script (dev/api...) will be trigger
the start of the CI/CD pipline till deploying on the production side.

### folder content:
    
* dev folder - has the developer scripts.
* prod folder - helm for deploying the app on the production side (k8s).deploy the "Talker" app. for more details [prod README.md](prod/README.md)
