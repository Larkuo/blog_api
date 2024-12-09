from marshmallow import validates, ValidationError
from marshmallow.validate import Length, Email
from app.extensions import ma, db
from app.models.user import User

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        # Prevents the schema from including password hash when dumping to JSON
        model = User

    id = ma.auto_field()
    username = ma.Str(required=True, validate=Length(min=3, max=80))
    email = ma.Str(required=True, validate=Email())
    password = ma.Str(load_only=True, required=True, validate=Length(min=8))
    role = ma.Str(required=True, validate=Length(min=3, max=80))

    @validates('username')
    def validate_username(self, value):
        # Ensure that the username doesn't already exist
        if db.session.get(User, username=value).first():
            raise ValidationError('Username already exists.')

    @validates('email')
    def validate_email(self, value):
        # Ensure that the email doesn't already exist
        if db.session.get(User, email=value).first():
            raise ValidationError('Email already exists.')
