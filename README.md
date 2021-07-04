# Backend Flask


## Migrations
```shell
$ python models.py
```


## Endpoints
```shell
curl --location --request POST 'http://127.0.0.1:9000/user' \
--header 'Content-Type: application/json' \
--data-raw '{
    "user_name": "rodrik",
    "password":  "password",
    "email": "rodrigo@gmail.com",
    "phone": "3104897244"
}'
```
