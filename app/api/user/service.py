from flask_jwt_extended import get_jwt_identity
from app.models.user import User


class UserService:
    @staticmethod
    def get_user_data(username: str):
        """
        Get User Data
        """

        current_user = get_jwt_identity()
        current_user_username = current_user['username']

        if username != current_user_username:
            return {
                'status': False,
                'message': 'Unauthorized Access',
            }, 400

        if not (user := User.query.filter_by(username=username).first()):
            return {
                'status': False,
                'message': 'User Not Found',
                'error_code': 'user_404',
            }, 404

        try:
            resp = {
                'status': True,
                'message': 'Retrieved user data',
                'user': {
                    'name': user.name,
                    'user_id': user.user_id,
                    'username': user.username,
                    'email': user.email
                }
            }
            return resp, 200
        except Exception as e:
            return {
                'status': False,
                'message': 'Internal Server Error',
                'error_code': 'server_error',
                'error': e
            }, 500
