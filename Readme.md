> *Server link Updated* 
## Server Link

 - [`Branch Details`](http://ec2-54-89-247-96.compute-1.amazonaws.com)

 
 - [`All Branch List`](http://ec2-54-89-247-96.compute-1.amazonaws.com/list)

## Sample Param:

#### Branch Details
 ```
 Branch Details param
 
	# input param:
		{
			"ifsc":"ABHY0065001"	
		}
	
	# output param:

	{
	    "status": true,
	    "data": {
		"user_data": {
		    "ifsc": "ABHY0065001",
		    "bank_name": "ABHYUDAYA COOPERATIVE BANK LIMITED",
		    "branch": "RTGS-HO",
		    "address": "ABHYUDAYA BANK BLDG., B.NO.71, NEHRU NAGAR, KURLA (E), MUMBAI-400024",
		    "city": "MUMBAI",
		    "district": "GREATER MUMBAI",
		    "state": "MAHARASHTRA"
		}
	    }
	}

													
 ```
 
#### All Branch Details
  ```
 All Branch List 
 
 	#Input param:
	{
		"bankName":"ABHYUDAYA COOPERATIVE BANK LIMITED",
		"city":"THANE"	
	}

	#output Param:
	
	{
    "status": true,
    "data": {
        "1": {
            "ifsc": "ABHY0065046",
            "bank_name": "ABHYUDAYA COOPERATIVE BANK LIMITED",
            "branch": "BHAYANDAR",
            "address": "SHOP NO. 7,8,9,&107 TO 111 ON GR. FLOOR & 1ST FLOOR. MALHAR ARCADE, CODDEV VILLAGE, NAVGHAR PHATAK ROAD, BHAYANDAR (E), DIST. THANE, 401101",
            "city": "THANE",
            "district": "THANE",
            "state": "MAHARASHTRA"
        },
        "2": {
            "ifsc": "ABHY0065048",
            "bank_name": "ABHYUDAYA COOPERATIVE BANK LIMITED",
            "branch": "KALYAN-WEST",
            "address": "FLOWER VALLEY, KHADAKPADA, KALYAN (W), DIST. THANE 421 301",
            "city": "THANE",
            "district": "THANE",
            "state": "MAHARASHTRA"
        },
	...
	...
	...
        "9": {
            "ifsc": "ABHY0065074",
            "bank_name": "ABHYUDAYA COOPERATIVE BANK LIMITED",
            "branch": "KAUSA MUMBRA",
            "address": "VIRANI BUSINESS CENTRE, SHOP NO. 1,2,3,4, PLOT NO. 96 BY 2, OPP BHARAT GEARS CO., KAUSA, DIST-THANE- 400612",
            "city": "THANE",
            "district": "THANE",
            "state": "MAHARASHTRA"
        }
    }
}


 ```
## Database Refrence

- [Indian Banks](https://github.com/snarayanank2/indian_banks)

## Setup Guide
 - create the new project
 - pull the project
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
