# Use the official Nginx image from Docker Hub
FROM nginx:latest

# Copy your HTML file into the Nginx container. the copy done on the docker-compose
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 for the container to be accessed
EXPOSE 80

# Run Nginx in the foreground (by default, it runs in the background)
CMD ["nginx", "-g", "daemon off;"]
