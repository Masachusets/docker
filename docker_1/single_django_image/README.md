Для создания docker-образа перейти в директорию api_with_restrictions и выполнить команду

```bush
docker build -t api_rest .
```

Для запуска контейнера

```bush
docker run -d -p 8000:8000 api_rest
```