<div align="center">

[//]: # (<img width="30%" src="https://user-images.githubusercontent.com/fav.PNG">)

# Travelling And Transport Services
</div>

#

## Overview

Web application based on flask.

First, User have to register here. then, registered users have the ability to book ride according their requirements. They can also book transport functionality.

Driver have to register here too. then, registered driver have the ability to add their vehicle details and make post for available to ride or transport. so user can book ride or transport functionality.

#

## Cloning the repository

=> Clone the repository using the command below :
```bash
git clone https://github.com/jaymind2810/travellingservice.git
```

=> Move into the directory where we have the project files : 
```bash
cd travellingservice
```

=> Create a virtual environment :
```bash
# Let's install virtualenv first
sudo apt install python3-venv

# Then we create our virtual environment
python3 -m venv venv
```

=> Activate the virtual environment :
```bash
source venv/bin/activate
```

=> Install the requirements :
```bash
pip install -r requirements.txt
```

#

## Running the App

=> To run the App, we use :
```bash
python3 Main.py
```

- Then, the development server will be started at http://127.0.0.1:2000/

=> If, there is any error running server then you can use to change port and try to run again

#

## Database :

=> Create Database name :
        
> travelingdb

#

## Create Admin Credential :

- You can create admin by command line.
> cd project
>
> flask --app=__init__.py create-admin


- You can also create admin login credential in "loginmaster" table Using INSERT query in Database table.

> sudo su - postgres
>
> psql
>
> \connect travelingdb
>
> INSERT INTO loginmaster VALUES (1, 'admin@gmail.com','admin','admin','active');
>
> SELECT * FROM loginmaster;

- Values are (loginId, loginUsername, LoginPassword, LoginRole, LoginStatus)

- loginRoles = [ 'admin', 'driver', 'user' ]

- loginStatus = [ 'active', 'inactive' ]



