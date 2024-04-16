import warnings
from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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



