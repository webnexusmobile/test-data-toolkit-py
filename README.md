# Evaluation of behave for test data creation via API

## Installation
```shell
pipenv install
```

## Excecution
```
pipenv run behave -D base_url="http://httpbin.org" -D username="user@example.com" -D password="secret"
```
or
```
BASE_URL="http://httpbin.org" pipenv runn behave
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

## Start server to enable remote execution via API call
```shell
flask run -p 4000
```

## Execute via API
```
curl -X POST -H 'Content-Type: application/json' -d '{"args": ["-D", "base_url=http://httpbin.org", "--tags", "@focus"}' http://localhost:4000/api/execute
```