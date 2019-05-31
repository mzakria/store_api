from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    paser =reqparse.RequestParser()
    paser.add_argument('price',
        type=float,
        required=True,
        help="this field is required !"

    )
    paser.add_argument('store_id',
        type=int,
        required=True,
        help="Every item needs store id !!"

    )

    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message':'Item not found'},404

    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exist".format(name)},400

        data = Item.paser.parse_args()
        item = ItemModel(name,**data)
        try:
            item.save_to_item()
        except:
            return {"message":"An Error Occurred"}, 500

        return item.json(), 201

    def delete(self,name):
        item = Item.find_by_name(name)
        if item:
            item.delete_form_db()

        return {'message':'Item deleted'}


    def put(self,name):
        data =Item.paser.parse_args()

        item =ItemModel.find_by_name(name)


        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']

        item.save_to_item()
        return item.json()

class ItemList(Resource):
    def get(self):
        return {'item':[item.json() for item in ItemModel.query.all()]}
