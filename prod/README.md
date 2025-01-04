# <p align="center">**Talker**</p>


this helm deploy the Talker app.
on a name space - Talker_dev:

             'helm upgrade --install -n talker-dev --create-namespace talker -f value.yaml .'
 
*Remove app:*
             'helm delete -n talker-dev talker'

   nginx load a image from dockerhub (standart nginx) and load a nginx.conf setting that are at the files directory.

## postgress:
    the app has a sql database. the data is on the nfs server (/data/db folder) for keeping the data consistency.
    db name : sec_db

## nginx:
    the app  uses nginx web server. the data is on the nfs server (/data/html).
    in folder files there is the index.html (should place on /usr/share/nginx/html).

## HTTPS:
   this app work in HTTPS ensuring secure webpage. the certificate is kept in a secret (ingress pull it and publish it)

## ARGO-CD:
   the app (talker) is deployed on ARGO-CD.
   to access:
   
            'kubectl port-forward svc/argo-cd-argocd-server 8080:80 -n argocd'
   
            'http://localhost:8080'
   
## CD stage:
  
    there are two main updates that can be done:
    - Flask api: update the api of the app by pulling the "latest" image from dockerhub. its done using ARGO-CD auto Updater. 
      the argo pull any new image post on the dockerhub with the "latest" tag and deply it automaticaly in the production.
    - HTML: update the content of the html files that deployed into the nginx servers (its located on a nfs server). the process 
      is done my a CronJob that is schudle to pull any new changes made on the folder nginxhtml on the repsitory.
