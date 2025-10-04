# Swipe&Go backend

## First time setup

```shell
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run locally

```shell
# Activate environment
source venv/bin/activate

flask run
```

This should open `http://127.0.0.1:5000` api. Test (i.e. in browser):

```
http://127.0.0.1:5000/test
```

## Creating new backend handlers

Handlers in `handlers` folder are named by the action they handle.
Each handler must contain:
1. class named `Model` (inherits from `pydantic.BaseModel`) - with fields this handler expects to see in request body
2. `handle` function with arguments:
    - `event` of type `Model` defined for this handler
    - `stores` of type `Stores` (container for different stores used by the handlers) - dependency injection pattern

## Usage - frontend

Hit the url:

```
https://hack-yeah-fastapi-mglkv.ondigitalocean.app/
```

## Notes
For future