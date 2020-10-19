[![Build Status](https://travis-ci.com/erayozer17/programming_ninja.svg?branch=master)](https://travis-ci.com/erayozer17/programming_ninja)

Common Commands

Build the images:
$ docker-compose -f docker-compose-dev.yml build

Run the containers:
$ docker-compose -f docker-compose-dev.yml up -d

Create the database:
$ docker-compose -f docker-compose-dev.yml run users python manage.py recreate_db

Seed the database:
$ docker-compose -f docker-compose-dev.yml run users python manage.py seed_db

Run the tests:
$ docker-compose -f docker-compose-dev.yml run users python manage.py test

To stop the containers:
$ docker-compose -f docker-compose-dev.yml stop

To bring down the containers:
$ docker-compose -f docker-compose-dev.yml down

To force a build
$ docker-compose -f docker-compose-dev.yml build --no-cache

Remove images:
$ docker rmi $(docker images -q)

To access the database via psql
$ docker exec -ti users-db psql -U postgres -W

Init db
$ docker-compose -f docker-compose-dev.yml run users python manage.py recreate_db

Seed db
docker-compose -f docker-compose-dev.yml run users python manage.py seed_db



Example docker-machine ec2 command

docker-machine create -d amazonec2 \
    --amazonec2-region us-west-2 \
    --amazonec2-instance-type "t2.micro" \
    --amazonec2-ssh-keypath ~/.ssh/ssh_key \
    aws-test
