# login

## Request 

Make a POST request to the `/login` endpoint with following payload:

```json
{
    "username": "<username>",
    "password": "<password>"
}
```

## Response

```json
{
  "token": "<auth-token>",
  "user_id": 13
}
```

Store the auth token and use it as part of all later requests!

User ID will usually NOT be needed, because backend knows the user id when the auth token is used in the request.
However, it may be useful in the future.
