# API MODULE

I created this API to make it easier for me to create something on various websites that I will create. So just call the API, no need to copy-paste from the previous code. Make the repo that will be created minimalist. Here I use python as the programming language and flask as the framework.

## Tech Stack

**Programming Language:** Python
**Library Framework:** Flask

## Running

run it with the following code

#### `flask --app main run --debug --port 5020`

## Pengguan API

Development Path

#### `http://127.0.0.1:5020/api/v1`

Production Path

#### `http://127.0.0.1:5020/api/v1`

### Route API

| Parameter    | Methods | Parameter                                    |
| :----------- | :------ | :------------------------------------------- |
| /geo-data    | GET     | Viewing all geo data that has been created   |
| /geo-data/id | GET     | Viewing geo data that has been created by id |
| /add-data    | POST    | create geo data                              |
| /update-data | PUT     | update geo data                              |
| /delete-data | DELETE  | delete geo data                              |

## Curl

/geo-data

```bash
curl --location 'http://127.0.0.1:5020/api/v1/geo-data?create_by=VOSSO-3010-ALJPB-82468HW-BVZDMSDJ6O-S9CAH' \
--header 'create_by: VOSSO-3010-ALJPB-82468HW-BVZDMSDJ6O-S9CAH'\'''
```

/geo-data/id

```bash
curl --location 'http://127.0.0.1:5020/api/v1/geo-data/VOGEO-3010-7SP2Z-8246FEQ-PT77V8LFRF-5J189' \
--header 'create_by: VOSSO-3010-ALJPB-82468HW-BVZDMSDJ6O-S9CAH'\'''
```

/add-data

```bash
curl --location 'http://127.0.0.1:5020/api/v1/add-data' \
--header 'Content-Type: application/json' \
--data '{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          106.95305568458355,
          -6.164570917511895
        ],
        "type": "Point"
      }
    }
  ]
}'
```

/update-data

```bash
curl --location --request PUT 'http://127.0.0.1:5020/api/v1/update-data/VOGEO-3010-7SP2Z-8246FEQ-PT77V8LFRF-5J189' \
--header 'Content-Type: application/json' \
--data '{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "kota": "Jakarta",
        "category":"MALL"
      },
      "geometry": {
        "coordinates": [
          106.95305568458355,
          -6.164570917511895
        ],
        "type": "Point"
      }
    }
  ]
}'


```

/delete-data

```bash
curl --location --request DELETE 'http://127.0.0.1:5020/api/v1/delete-data/VOGEO-3010-7SP2Z-8246FEQ-PT77V8LFRF-5J189' \
--header 'Content-Type: application/json'
```

## Authors

- [@movinoary](https://github.com/movinoary?tab=repositories)
