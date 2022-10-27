upstream backend {
    server app:8000:
}

server {
    listen 80;

    location / {
        proxy_pass http://backend;
    }
}