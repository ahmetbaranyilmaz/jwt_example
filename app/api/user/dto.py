from flask_restx import Namespace, fields


class UserDto:
    api = Namespace("<string:username>", description="User Related Operations")

    user = api.model("User Model", {
        "email": fields.String,
        "name": fields.String,
        "username": fields.String
    })

    data_resp = api.model("User Data Response", {
        "status": fields.Boolean,
        "message": fields.String,
        "user": fields.Nested(user)
    })
