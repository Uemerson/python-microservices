# About

A simple Microservices example with Python Django and Python Flask.

# How to run django app?

To run [admin](admin) app, follow steps below:

```
$ docker-compose up --build
```

Run migrations:

```
$ docker-compose exec backend sh
```

```
$ python manage.py migrate
```

After apply migrate run again:

```
$ docker-compose up --build
```

To create migrations:

```
$ python manage.py makemigrations
```

# How to run flask app?

To run [main](main) app, follow steps below:

```
$ docker-compose up --build
```

Run migrations with `flask-cli`:

```
$ docker-compose exec backend sh
```

```
$ flask db upgrade
```

After apply migrate run again:

```
$ docker-compose up --build
```

To create migrations:

```
$ flask db migrate
```