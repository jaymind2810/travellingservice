<div align="center">

[//]: # (<img width="30%" src="https://user-images.githubusercontent.com/fav.PNG">)

# Travelling And Transport Services
</div>

### Cloning the repository

--> Clone the repository using the command below :
```bash
git clone https://github.com/jaymind2810/travellingservice.git

```

--> Move into the directory where we have the project files : 
```bash
cd travellingservice

```

--> Create a virtual environment :
```bash
# Let's install virtualenv first
sudo apt install python3-venv

# Then we create our virtual environment
python3 -m venv venv

```

--> Activate the virtual environment :
```bash
source venv/bin/activate

```

--> Install the requirements :
```bash
pip install -r requirements.txt

```

#

### Running the App

--> To run the App, we use :
```bash
python3 Main.py

```

> ⚠ Then, the development server will be started at http://127.0.0.1:2000/

--> If, there is any error running server then you can use to change port and try to run again

[//]: # (#)

[//]: # ()
[//]: # (### App Preview :)

[//]: # ()
[//]: # (<table width="100%"> )

[//]: # (<tr>)

[//]: # (<td width="50%">      )

[//]: # (&nbsp; )

[//]: # (<br>)

[//]: # (<p align="center">)

[//]: # (  Feed Home)

[//]: # (</p>)

[//]: # (<img src="https://user-images.githubusercontent.com/7.PNG">)

[//]: # (</td> )

[//]: # (<td width="50%">)

[//]: # (<br>)

[//]: # (<p align="center">)

[//]: # (  Room Conversation Preview)

[//]: # (</p>)

[//]: # (<img src="https://user-images.githubusercontent.com/72341.PNG">  )

[//]: # (</td>)

[//]: # (</table>)


#

### Database :

--> Create Database name :
        
> travelingdb


--> Create Admin login credential in "loginmaster" table Using INSERT query in Database table.

> sudo su - postgres

> psql

> \connect travelingdb

> INSERT INTO loginmaster VALUES (1, 'admin@gmail.com','admin','admin','active');

- (loginId, loginUsername, LoginPassword, LoginRole, LoginStatus)

- loginRoles = [ 'admin', 'driver', 'user' ]

- loginStatus = [ 'active', 'inactive' ]

> SELECT * FROM loginmaster;


