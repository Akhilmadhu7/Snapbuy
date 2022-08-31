server {
    listen 80;
    server_name snapbuy.website;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        autoindex on;
        alias /home/ubuntu/newproject/ebazaar/static/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}