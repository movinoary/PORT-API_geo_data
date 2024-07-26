# API MODULE
I created this API to make it easier for me to create something on various websites that I will create. So just call the API, no need to copy-paste from the previous code. Make the repo that will be created minimalist. Here I use python as the programming language and flask as the framework.

## Running

run it with the following code
#### `flask --app main run --debug --port 5020`


## Pengguan API

Development Path

#### `http://127.0.0.1:5020/api/v1`

Production Path

#### `http://127.0.0.1:5020/api/v1`

### Route API

| Parameter            | Methods | Parameter                                  |
| :------------------- | :------ | :----------------------------------------- |
| /geo-data            | GET     | Viewing all geo data that has been created |
| /geo-data/id         | GET     | Viewing geo data that has been created by id  |
| /add-data            | POST    | create geo data |
| /update-data         | PUT     | update geo data |
| /delete-data         | DELETE  | delete geo data |
