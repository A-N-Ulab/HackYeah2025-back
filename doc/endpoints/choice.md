# Delete trip

Make a POST request to the `/choice` endpoint with following payload:

## Request

```json
{
    "token": "<auth-token>",
    "trip_id": 3,
    "destination_id": 4,
    "choice": true
}
```

Use `choice` as False when swapped left (rejected),
Use True when swapped right (accepted).

## Response
```json
{
    "choice_idx": 3,
    "total_choices": 15
}
```

`choice_idx` is the amount of choices already completed.

`total_choices` is the total amount of all choices to be made in the survey.
