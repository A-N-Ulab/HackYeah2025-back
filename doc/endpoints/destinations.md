# Destinations

## Request 

Make a POST request to the `/destinations` endpoint with following payload:

```json
{
    "token": "<auth-token>",
    "trip_id": 13
}
```

## Response

```json
{
  "is_survey": true,
  "destinations": [
    {
      "id": 13,
      "name": "Baltic Sea",
      "description": "Some place description",
      "photo_name": "test.png",
    }
  ]
}
```

The field `is_survey` will be True when it's the first time setup for this trip.
Until the survey is completed, the flag will always be set `true` for this trip.

When the survey is completed, every next request to this endpoint will return
this flag as `false`, for the given trip.

`destinations` contains a list of destinations to display. Destination ID is crucial, 
as it's the part of the feedback request, to let backend know of the decision user has made about this destination.

`name` and `descriptions` are to be displayed to the user.

`photo_name` is a name of the file, including the extension.

The image must be downloaded separately.
