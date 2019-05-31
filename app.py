from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT

from resources.user import UserRegistor
from resources.item import Item, ItemList
from security import authenticate, identity
from resources.store import Stores, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.secret_key = 'me'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app,authenticate,identity) #/auth


api.add_resource(Item,'/item/<string:name>')
api.add_resource(Stores,'/store/<string:name>')

api.add_resource(ItemList,'/items')
api.add_resource(StoreList,'/stores')

api.add_resource(UserRegistor,'/registor')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)
