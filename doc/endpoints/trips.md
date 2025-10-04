# Return all trips connected with user

Make a POST request to the `/trips` endpoint with following payload:

## Request

```json
{
    "token": "<auth-token>"
}
```

## Response
```json
{
    "trips": [
        {
            "description": "moj dlogi opis",
            "id": 3,
            "name": "nowy opis"
        },
        {
            "description": "moj drogi opis",
            "id": 4,
            "name": "nowa destynacja"
        }
    ]
}
```

