# Remuner backend

This project has been produced as technical probe for Remuner. It uses FastAPI, PostgresDB and Redis.

<details>
    <summary>Running the project</summary>

#### Build
```bash
docker-compose build
```

#### Launch
For a standalone launch, run:
```bash
docker-compose up -d remuner-frontend
```
If this is supposed to work locally with the frontend running in docker, launch:
```bash
docker-compose up -d remuner-frontend-dev
```
</details>

<details>
    <summary>Methodology</summary>

The project follows the following industry trends:
1. [Hexagonal architecture](https://www.happycoders.eu/software-craftsmanship/hexagonal-architecture/)

In order to improve the scalability and maintainability of the project, this architecture has been followed in order to isolate the business logics from the API and the persistences.

2. [SOLID](https://www.digitalocean.com/community/conceptual-articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design)

Serializers and business objects are declared on one side while controllers and services on the other. 
Interfaces are defined for persistences so they can easily be exchanged. 

3. Version control

There are two levels of versioning. One is implemented both at route and header level to handle major and minor versions. This allows to change the API witohut breaking any existing integration for a given business architecture. In case the whole core wants to be changed, it is possible to do so at path level.

</details>

<details>
    <summary>Design decisions</summary>
- An integration must have a user
- The token is registered but never returned. Hence, if a token is edited, the old one is erased. This works in the same way as AWS access tokens (can't be recovered after generation)
- Users with active integrations can't be erased
</details>

<details>
    <summary>Folder structure</summary>

- Users and integrations have been separated in different apps. This way, we guarantee domain isolability and open the door to break the repo in two different microservices.
- Tortoise has been used as ORM
- Each app has 4 different folders to differentiate the domain layer on one side, API/database adapters on an the other and the dependency injection betweem them in the last one.
- The domain defines the interfaces needed (that are implemented in the corresponding package in an independent way).

Since it was a small project, it was the input/output mapping services have been defined both in `common` and `crud` to show how the structure should look like. Nevertheless, in this case, all mappings should go in common since there are no particularities.

Two database implementations are done for the persistences and can be transparently interchanged through the dependency injection (since they share the same interface).

</details>

<details>
    <summary>Tests</summary>

Tests are organized in a similar way as the repository. In addition, factories and fixtures are declare to speed up the test creation.
Each test uses a Postgres instance so they don't interact between them. The use of the persistence services is encouraged instead of the ORM to avoid depending on a certain implementation.
Tests can be run with the following command:
```
docker-compose run --rm test 
```

</details>

<details>
    <summary>Other comments</summary>

Everything is fully containerized, making it really easy to integrate with cloud providers as AWS as long as CircleCI/github actions for the automatic testing and merging control.

Code formatting can be done with the following command:

```
docker-compose run --rm format
```

It is performed following PEP8 using `ruff` and `black`.

</details>

<details>
    <summary>Known problems and future work</summary>
No type verification is done (mails should be emails, for example). These verifications should be done both in the backend and the frontend.

In the frontend, the error handling should improve, better informing the user by capturing the coded errors.

The cached version of the persistence is implemented to show how different elements can be inserted and how different persistences can be exchanged.
Nevertheless, there are several problems with the current implementation:
- The initialization process should be improved with locks to ensure it is correct
- Tests should initialize an other redis (they interact with the running instance in case is running)
</details>