from flask import request
from flask_restx import Resource
from .service import AuthService
from .dto import AuthDto
from .utils import LoginSchema, RegisterSchema

api = AuthDto.api
auth_success = AuthDto.auth_success
login_model = AuthDto.login_model
register_model = AuthDto.register_model

login_schema = LoginSchema()
register_schema = RegisterSchema()


@api.route("/login")
class AuthLogin(Resource):
    """
    User Login Endpoint
    User requests a token to be used in future requests
    """

    @api.doc("Auth Login", responses={
        200: "Success",
        400: "Validation Error",
        403: "Invalid Credentials",
        404: "User Not Found"
    })
    @api.expect(login_model, validate=True)
    def post(self):
        """
        User Login
        """
        login_data = request.get_json()

        if errors := login_schema.validate(login_data):
            return {
                'status': False,
                'errors': errors
            }, 400
        return AuthService.login(login_data)


@api.route("/register")
class AuthRegister(Resource):
    """
    User Registration Endpoint
    User requests a token to be used in future requests
    """

    @api.doc("Auth Register", responses={
        200: "Success",
        400: "Validation Error",
        409: "Email or Username already exists"
    })
    @api.expect(register_model, validate=True)
    def post(self):
        """
        User Registration
        """
        register_data = request.get_json()

        if errors := register_schema.validate(register_data):
            return {
                'status': False,
                'errors': errors
            }, 400
        return AuthService.register(register_data)
