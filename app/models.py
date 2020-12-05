from .import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):

    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255),unique=True)
    email=db.Column(db.String(255),unique=True,index=True)
    pass_secure=db.Column(db.String(255))
    bio=db.Column(db.String(255))
    profile_pic_path=db.Column(db.String(255))
    postes=db.relationship('Post',backref='user',lazy="dynamic")
    comment=db.relationship('Comment',backref='user',lazy="dynamic")



    @property
    def password(self):
        raise AttributeError('you cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure=generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure,password)
    def save_u(self):
        db.session.add(self)
        db.session.commit()
    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()

    def __repr__(self):
        return f'User{self.username}'

class Post(db.Model):

    __tablename__='postes'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(255),nullable = False)
    post=db.Column(db.Text(),nullable = False)
    category=db.Column(db.String(255),index=True)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))

    comment=db.relationship('Comment',backref='post',lazy="dynamic")


    def save_p(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Post {self.post}'

class Comment(db.Model):
    __tablename__='comments'
    id=db.Column(db.Integer,primary_key=True)
    comment=db.Column(db.Text())
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    post_id=db.Column(db.Integer,db.ForeignKey('postes.id'))

    def save_c(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,post_id):
        comments=Comment.query.filter_by(post_id=id).all()
        return comments

    def __repr__(self):
        return f'comment{self.comment}'

class Quotes:
    def __init__(self,author,quote):
        '''
        class of Quote
        '''
        self.author=author
        self.quote=quote
