# MeliChallenge

# About the Project.


## Built With.

- Python 3.11
- Flask
- Docker

---

# Initializing Project.

## Pre-requisites

### Technologies Used.

- **Docker**

    [Get Started With Docker](https://www.docker.com/get-started/)


- **Flask**

    [Installation - Flask](https://flask.palletsprojects.com/en/3.0.x/installation/)

---

### Environment Vars.

MONGO_URI=mongodb://db/reto_meli
BASE_API_URL=https://api.mercadolibre.com/


FILE_NAME=/files/technical_challenge_data.csv
SEPARATOR=,
ENCODING=utf-8
BATCH_SIZE=10
THREADS_NUMBER=20  # Number of threads that will be using the application to make requests.

- **MONGO_URI:** This variable is the connection to the mongo database, it is in this form so that it connects via docker, preferably leave as is
- **BASE_API_URL:** Variable used to store MeLi api address
- **FILE_NAME:** FILE_NAME must have the full path in this case as we are using docker must be like this: '/files/{name_of_file}' to work properly, and the file must be inside files folder.
- **SEPARATOR:** Separador de data en archivos de texto
- **ENCODING:** Encoding used in the text file
- **BATCH_SIZE:** Batch size used when reading the text file to process data in batches
- **THREADS_NUMBER:** Number of threads that will be used when querying the API to speed up the process


| ENV_VAR | Value |
| --- | --- |
| **MONGO_URI** | mongodb://db/reto_meli |
| **BASE_API_URL** | https://api.mercadolibre.com/ |
| **FILE_NAME** | /files/technical_challenge_data.csv |
| **SEPARATOR** | , |
| **ENCODING** | utf-8 |
| **BATCH_SIZE** | 20 |
| **THREADS_NUMBER** | 20 |

---

# Execution of the Project Testing/Developing.

### Run with docker

Be sure you have docker installed, then open the console and type:

```sh
docker-compose up --build
```

This command will run the project, it means that docker will execute the mongo database and the project itself.

Once the docker container is up you can go ahead and try the endpoints.


## Endpoints


- ### [GET] localhost:8000/process

This endpoint will execute the full program, it will read the file and then do the requests to MeLi's API.

```sh
curl --location 'localhost:8000/process'
```

- ### [GET] localhost:8000/find_one/'id'

This endpoint will bring information if exists of saved items.

example:
```sh
curl --location 'localhost:8000/find_one/MLA828617220'
```
---

## Project Structure


# Contact

Alejandro Uribe - alejo.uribe35@gmail.com
