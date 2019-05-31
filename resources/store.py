from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.store import StoreModel

class Stores(Resource):
    paser =reqparse.RequestParser()
    paser.add_argument('price',
        type=float,
        required=True,
        help="this field is required !"

    )
    paser.add_argument('store_id',
        type=float,
        required=True,
        help="Every item needs store id !!"

    )

    @jwt_required()
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message':'Store not found'},404

    def post(self,name):
        if StoreModel.find_by_name(name):
            return {'message': "An item with name '{}' already exist".format(name)},400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message":"An Error Occurred"}, 500

        return store.json(), 201

    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_form_db()

        return {'message':'store deleted'}


class StoreList(Resource):
    def get(self):
        return {'stores':[store.json() for store in StoreModel.query.all()]}
