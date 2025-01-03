create a Nginx web server with the speech to text file as index.html
listen on port 80 
to build:
docker build -t nginx-html .
to run:
docker run -d -p 8080:80 --name my-nginx-container nginx-html
to open the web page:
http://localhost:8080


Docker Compose (Optional)

docker-compose up -d
