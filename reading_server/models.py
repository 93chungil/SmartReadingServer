from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64) ,index=True,unique=True)
    email = db.Column(db.String(120) ,index=True,unique=True)
    picturepath = db.Column(db.String(128), index= True)

    password_hash = db.Column(db.String(128))

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash , password)

    def getJsonData(self):
        return {"username" : self.username, 
                "email" : self.email}

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class Group(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    groupname = db.Column(db.String(120) ,index=True,unique=True)
    picturepath = db.Column(db.String(120), index= True)
   
    def getJsonData(self):
        return {"groupname" : self.username}

    def __init__(self, groupname):
        self.groupname= groupname

    def __repr__(self):
        return '<Group %r>' % self.groupname

class UserGroup(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key = True)
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"), primary_key = True)

    user = db.relationship("User", foreign_keys=user_id)
    group = db.relationship("Group", foreign_keys=group_id)

    def __init__(self, user_id, group_ide):
        self.user_id = user_id
        self.group_id = group_id
