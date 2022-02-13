from flask_jwt_extended import create_access_token
from app import db
from app.models.user import User


class AuthService:
    @staticmethod
    def login(data: dict):
        email = data.get('email')
        password = data.get('password')
        try:
            if not (user := User.query.filter_by(email=email).first()):
                return {
                           'status': False,
                           'message': 'Email not exist',
                           'error_code': 'email_404'
                       }, 404
            elif user and user.verify_password(password):
                identity = {
                    "user_id": user.user_id,
                    "username": user.username
                }

                access_token = create_access_token(identity=identity)
                resp = dict(
                    status=True,
                    message='Login Success',
                    access_token=access_token,
                    user={
                        'user_id': user.user_id,
                        'username': user.username,
                        'email': user.email,
                        'name': user.name
                    }
                )
                return resp, 200
            return {
                       'status': False,
                       'message': 'Wrong email or password',
                       'error_code': 'email_password_404'
                   }, 404

        except Exception as e:
            return {
                'status': False,
                'message': 'Internal Server Error',
                'error_code': 'server_error',
                'error': e
            }, 500

    @staticmethod
    def register(data: dict):
        email = data.get('email')
        username = data.get('username')
        name = data.get('name')
        password = data.get('password')

        if User.query.filter_by(email=email).first():
            return {
                       'status': False,
                       'message': 'This email is used',
                       'error_code': 'email_409'
                   }, 409
        elif User.query.filter_by(username=username).first():
            return {
                       'status': False,
                       'message': 'This username is used',
                       'error_code': 'email_409'
                   }, 409

        try:
            user = User(email=email,
                        username=username,
                        name=name,
                        password=password)

            db.session.add(user)
            db.session.commit()

            identity = {
                "user_id": user.user_id,
                "username": username
            }

            access_token = create_access_token(identity=identity)
            resp = dict(
                status=True,
                message='Login Success',
                access_token=access_token,
                user={
                    'user_id': user.user_id,
                    'username': user.username,
                    'email': user.email,
                    'name': user.name
                }
            )
            return resp, 200
        except Exception as e:
            return {
                'status': False,
                'message': 'Internal Server Error',
                'error_code': 'server_error',
                'error': e
            }, 500
