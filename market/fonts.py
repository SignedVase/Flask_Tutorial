from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User
from market import db
from sqlalchemy import select


class RegisterForm(FlaskForm):

    def validate_username(self, usr_check):
        stmt = select(User).where(User.username == usr_check.data)
        user = db.session.scalar(stmt)
        if user:
            raise ValidationError("Usuário já existe! Utilize outro nome.")

    def validate_email_address(self, email_check):
        stmt = select(User).where(User.email_address == email_check.data)
        email = db.session.scalar(stmt)
        if email:
            raise ValidationError("Endereço de E-mail ja cadastrado! Utilize outro e-mail.")

    username = StringField(label='User Name:', validators=[Length(min=3, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=8), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='submit')