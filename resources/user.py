from flask_restful import Resource,reqparse
from models.user import UserModel

class UserRegistor(Resource):
    paser =reqparse.RequestParser()
    paser.add_argument('username',
        type=str,
        required=True,
        help="this field is required !"
    )
    paser.add_argument('password',
        type=str,
        required=True,
        help="this field is required !"
    )

    def post(self):
        data = UserRegistor.paser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "A user already exist"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "user created successfuly"},201
