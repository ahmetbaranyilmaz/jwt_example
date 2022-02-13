from flask_restx import Namespace, fields


class AuthDto:
    api = Namespace('auth', description='Authentication related operations')

    user_model = api.model('User Model', {
        "email": fields.String,
        "name": fields.String,
        "username": fields.String
    })

    login_model = api.model('Login Model', {
        "email": fields.String(required=True, description="User email address"),
        "password": fields.String(required=True, description="User password")
    })

    register_model = api.model('Register Model', {
        "email": fields.String(required=True, description="User email address"),
        "username": fields.String(required=True, description="User username"),
        "name": fields.String(required=True, description="User name"),
        "password": fields.String(required=True, description="User password")
    })

    auth_success = api.model('Auth Success Response', {
        "status": fields.Boolean,
        "message": fields.String,
        "access_token": fields.String,
        "user": fields.Nested(user_model)
    })
