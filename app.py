from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Create tables


app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

from routes import *
if __name__ == "__main__" :
    app.run(debug=True)