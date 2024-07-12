# Temperature gauge for home when we're not at home

Containterized Flask app to read API, parse JSON and show the temperature reading

Uses the API that [lpgera/argus](https://github.com/lpgera/argus/) data collector application provides

## Project structure:

```
.
├── compose.yaml
├── .env
└── app
    ├── Dockerfile
    ├── requirements.txt
    ├── app.py
    └── templates
        └──  temp.html
```

## Deploy with docker compose

```
$ docker compose up -d
```

## TODO
- [x] MVP
- [ ] Draw an actual gauge
