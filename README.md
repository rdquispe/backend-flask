# backend-flask


```
$ pip install -r requirements.txt

Migracion

$ python models.py
```


## endpoint
```shell
curl --location --request POST 'http://127.0.0.1:9000/user' \
--header 'Content-Type: application/json' \
--data-raw '{
    "user_name": "user_name",
    "password":  "password"
}'
```
