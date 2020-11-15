# Evaluation of behave for test data creation via API

## Installation
```shell
pip install -r requirements.txt
```

## Excecution
```
behave -D base_url="http://httpbin.org" -D username="user@example.com" -D password="secret"
```
or
```
BASE_URL="http://httpbin.org" behave
```

## Excecute only scenarios with @focus tag
```shell
behave -D base_url="http://httpbin.org" --tags="@focus"
```

## Build docker container
```shell
docker build . -t test-data-toolkit:latest
```

## Dockerized execution
```shell
docker run -it test-data-toolkit:latest -D base_url="http://httpbin.org"
```

## Dockerized execution with tags
```shell
docker run -it test-data-toolkit:latest -D base_url="http://httpbin.org" --tags="@focus"
```

## Execute local changes in container
```shell
docker run -v ${pwd}/features:/home/worker/features -it -e BASE_URL=http://httpbin.org test-data-toolkit:latest
```

## Start server
flask run -p 4000

## Execute via API
```
curl -X POST -H 'Content-Type: application/json' -d '{"args": ["-D", "base_url=http://httpbin.org", "--tags", "@focus"}' http://localhost:4000/api/execute
```