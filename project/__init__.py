import warnings
from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import click
import re

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

app = Flask(__name__)

app.secret_key = 'sessionData'

app.config['TESTING'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True                                   

# app.config['SQLALCHEMY_ECHO'] = True that is used to Sqlalchemy query log in terminal
app.config['SQLALCHEMY_ECHO'] = False
# app.config['SQLALCHEMY_ECHO'] = True

app.config['SQLALCHEMY_RECORD_QUERIES'] = True

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3307/pythondb'

# =================== Postgeresql Setup ====================================
# DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/travelingdb"


db = SQLAlchemy(app)

app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

import project.com.controller


from project.com.vo.LoginVO import LoginVO
from project.com.dao.LoginDAO import LoginDAO

@app.cli.command("create-admin")
def create_user():
    username = input("Enter your email or username: ")
    password = input("Enter your password: ")
    password1 = input("Again, Confirm your password: ")

    email_regex = r"^[^@]+@[^@]+\.[^@]+$"

    if bool(re.match(email_regex, username)) is False:
        app.logger.error('Email address is not valid.')
        return

    if password != password1:
        app.logger.error('Password is not match.')
        return

    loginVO = LoginVO()
    loginDAO = LoginDAO()

    loginVO.loginUsername = username
    loginVO.loginPassword = password
    loginVO.loginRole = "admin"
    loginVO.loginStatus = "active"
    loginDAO.insertLogin(loginVO)

    print("Admin loginId", loginVO.loginId)

    app.logger.info('Admin login credential created.')


# @app.cli.command("create-user")
# @click.argument("name")
# def create_user(name):
#     print("Herer--------In Command---------", name)


