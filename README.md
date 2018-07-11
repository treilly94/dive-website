[![Build Status](https://travis-ci.org/treilly94/dive-website.svg?branch=development)](https://travis-ci.org/treilly94/dive-website)
# dive_website

## Starting the development server
Navigate to the diveguide directory and run  
```
python manage.py runserver
```

## Starting docker compose
The docker compose files were made based on [this tutorial](https://docs.docker.com/compose/django/#connect-the-database).
The containers can be started using the below command:  
```
docker-compose up
```
And stopped using the below command:
```
docker-compose down
```
Once the containers are both up the tables will need to be migrated onto the database. This can be done by running the 
below command on the web server:  
```
python divesite/manage.py migrate
```