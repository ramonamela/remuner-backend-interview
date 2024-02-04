aerich init -t app.database.TORTOISE_ORM
aerich init-db

## Remove database
#  docker volume ls | grep postgres | grep remuner | awk '{ print $2 }' | xargs docker volume rm
#  docker volume ls | grep cache | grep remuner | awk '{ print $2 }' | xargs docker volume rm
