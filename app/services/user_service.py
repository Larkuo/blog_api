from app.models.user import User
from app.extensions import db

def get_user_by_id(id):
    return db.session.get(User, id=id)

def get_user_by_username(value):
    return db.session.get(User, username=value).first()

def get_user_by_email(value):
    return db.session.get(User, email=value).first()

def create_new_user(data):    
    new_user = User(username=data['username'], email=data['email'], role=data['role'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()

    return new_user

def update_user_by_id(user_id, data):
    user = db.session.get(User, user_id).first()

    for key, value in data.items():
        setattr(user, key, value)
    
    db.session.commit()
    return user

def delete_user_by_id(user_id):
    user = db.session.get(User, user_id)
    db.session.delete(user)
    db.session.commit()