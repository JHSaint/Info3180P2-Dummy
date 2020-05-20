from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')

class ProfileForm(FlaskForm):
    first_name = StringField('First Name', validators = [DataRequired()])
    last_name = StringField('Last Name', validators = [DataRequired()])
    username = StringField('Username', validators = [DataRequired()])
    password = StringField('Password',validators = [DataRequired()])
    email = StringField('Email',validators = [DataRequired(),Email()])
    location = StringField('Location', validators = [DataRequired()])
    bio = TextAreaField('bio', validators = [DataRequired()])
    pic = FileField('Profile Picture', validators = [FileRequired(), FileAllowed(['jpg','jpeg','png'], 'Only images please.')])
    submit = SubmitField("Add Profile")
