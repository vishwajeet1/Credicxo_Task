## Server Link

 - [`Branch Details`](http://34.228.119.210/)
 ```
 Branch Details param
 
     #param:
         {
             "ifsc":"ABHY0065001"	
             }
 ```
 
 - [`All Branch List`](http://34.228.119.210/list)
  ```
 All Branch List 
 
     #param:
         {
            "bankName":"BANK OF BARODA",
            "city":"DELHI"
             }
 ```
 

## Setup Guide
 - create the new project
 - clone the project
 - install and create a virtual environment

```
#!bash
    pip install virtualenv
    virtualenv {environment_name}
    sudo chmod 777 /{environment_name}
```

 - activate the environment with command line `source/{environment_name}/activate`
 - install all the requirements from `requirement.txt` by running the file Command line

```
#!bash
    pip install -r requirements.txt
```

 - install local database postgres version `(PostgreSQL) 
 - create a user
 - create a database
 - give permissions to access database to newly created user
 - setup all the database credentials in inclov/settings/base.py
 - Initiate database by command

```
#!bash

    postgres -D /usr/local/var/postgres
```

 - after setting up the database hit a command on terminal


```
#!bash

    python manage.py makemigrations
    python manage.py migrate
```


```
#!bash
    python manage.py runserver

```

```
#!bash
    install requirements
    add django_crontab in settings
    python manage.py crontab add


```
