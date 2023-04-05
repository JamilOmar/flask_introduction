# apps.members.models

from datetime import datetime

from .shared import db
class Todo(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200) , nullable=False)
    date_created = db.Column(db.DateTime,default = datetime.utcnow)

    def __repr__(self) -> str:
        return '<Task {}>'.format(self.id)