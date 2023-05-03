# Backend Flask


## Migrations
```shell
$ python models.py
```


## Endpoints
```shell
curl --location --request POST 'http://localhost:9000/user' \
--header 'Content-Type: application/json' \
--data-raw '{
    "user_name": "rodrigo",
    "password":  "password",
    "email": "some@mail.com",
    "phone": "123456789"
}'
```
