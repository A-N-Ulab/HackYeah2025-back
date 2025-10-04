# Delete trip
Make a POST request to the `/delete_trip` endpoint with following payload:
## Request

```json
{
    "token": "<auth-token>",
    "id": 3
}
```

## Response
```json
{
    "id": 3
}