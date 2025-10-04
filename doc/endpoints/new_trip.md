# Create new trip

## Request

Make a POST request to the `/new_trip` endpoint with following payload:

```json
{
    "token": "<auth-token>",
    "name": "My new trip name",
    "description": "Trip description"
}
```

## Response
```json
{
    "id": 3
}
```
Returns trip id if OK, or 403 error code, if the token doesn't exists
