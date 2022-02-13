from flask_restx import Resource
from flask_jwt_extended import jwt_required
from .service import UserService
from .dto import UserDto

api = UserDto.api
data_resp = UserDto.data_resp


@api.route("")
class UserGet(Resource):
    @api.doc("Get Specified User Data", responses={
        200: ("Success", data_resp),
        404: "User Not Found",
        400: "Unauthorized Access"
    })
    @jwt_required()
    def get(self, username: str):
        """
        Get user info
        :param username:
        """
        return UserService.get_user_data(username)
