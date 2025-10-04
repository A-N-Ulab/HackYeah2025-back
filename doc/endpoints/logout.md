# login

## Request

Make a POST request to the `/logout` endpoint with following payload:

```json
{
    "token": "<auth-token>"
}
```

## Response

```json
{}
```

Returns empty body if OK, or 403 error code, if the token doesn't exists

This request simply deletes the token.
