Для создания docker-образа

```bush
docker build -t newnginx .
```

Для запуска контейнера

```bush
docker run -d -p 8080:80 newnginx
```