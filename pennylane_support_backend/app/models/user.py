from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    auth0_id = db.Column(db.String(255), unique=True, nullable=False) 

    def __repr__(self):
        return f"<User {self.username}>"
