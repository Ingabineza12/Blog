from flask_wtf import  FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField
from wtforms.validators import Required


class UpdateBlogForm(FlaskForm):
    title=StringField('Title', validators=[Required()])
    category=SelectField('Category',choices=[('Music','Music'),('Job','Job'),('News','News')], validators=[Required()])
    post=TextAreaField('Your Post.', validators=[Required()])
    submit=SubmitField('save')

class PostForm(FlaskForm):
    title=StringField('Title', validators=[Required()])
    category=SelectField('Category',choices=[('Music','Music'),('Job','Job'),('News','News')], validators=[Required()])
    post=TextAreaField('Your Post', validators=[Required()])
    submit=SubmitField('Post')

class CommentForm(FlaskForm):
    comment=TextAreaField('Leave a comment',validators=[Required()])
    submit=SubmitField('Comment')
