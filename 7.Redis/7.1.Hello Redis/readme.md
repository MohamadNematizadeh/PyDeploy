  <h2 align="center"> 7.1.Hello Redis </h2></h2>
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

### Install the Redis Python client by running
```
pip install redis
```

## How to run:
Run in file `` main.ipynb  ``
