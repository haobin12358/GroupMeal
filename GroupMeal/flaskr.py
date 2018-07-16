# *- coding:utf8 *-
from flask import Flask
import flask_restful
from GroupMeal.apis.AMeals import GMMeals
from GroupMeal.apis.AUsers import GMUsers
from GroupMeal.apis.AMess import GMMess
from GroupMeal.apis.ACarts import GMCarts
from GroupMeal.apis.AOrders import GMOrders

gm = Flask(__name__)
api = flask_restful.Api(gm)

api.add_resource(GMUsers, "/group/meal/user/<string:users>")
api.add_resource(GMMeals, "/group/meal/meal/<string:meals>")
api.add_resource(GMMess, "/group/meal/mess/<string:mess>")
api.add_resource(GMCarts, "/group/meal/cart/<string:cart>")
api.add_resource(GMOrders, "/group/meal/order/<string:orders>")

'''
if __name__ == '__main__':
    gm.run('0.0.0.0', 443, debug=True, ssl_context=(
        "/etc/nginx/cert/1525609592348.pem"
    ))
'''
if __name__ == '__main__':
    gm.run('0.0.0.0', 7444, debug=True)
