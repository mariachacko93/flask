# from reg import db
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

from datetime import datetime

class User(db.Model):
    id=db.Column(db.Integer)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(20),unique=True,nullable=False)
    password=db.Column(db.String(20),nullable=False)
    date_created=db.Column(db.DateTime(20),default=datetime.utcnow)

    def __rep__(self):
        return self.username
