  <h2 align="center"> 7.2.Hello Celery </h2></h2>
  <p align="center" ><img src = "https://skillicons.dev/icons?i=py,redis,docker"></p>


## Setup Redis Server Docker:
Pull and run the Redis image from Docker Hub :
```
docker pull redis
```

```
docker run --name redis -d -p 6379:6379 redis
```
Verify that Redis is running by connecting to it :
```
docker exec -it redis redis-cli
```

## How to Install :
```
pip install "redis" "celery" "fastapi[standard]"
```

## How to run:
Run celery in file celery_tasts.py
```
celery --app celery_tasts worker --concurrency=1 --loglevel=DEBUG
```
run fastAPI in file api.py
```
uvicorn api:app 
```
