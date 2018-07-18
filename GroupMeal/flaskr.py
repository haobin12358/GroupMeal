# *- coding:utf8 *-
from flask import Flask
import flask_restful
from GroupMeal.apis.AMeals import GMMeals
from GroupMeal.apis.AUsers import GMUsers
from GroupMeal.apis.AMess import GMMess
from GroupMeal.apis.ACarts import GMCarts
from GroupMeal.apis.AOrders import GMOrders
from GroupMeal.apis.AReview import GMReview
from GroupMeal.apis.ACoupons import GMCoupons
from GroupMeal.apis.AOther import GMOther
from GroupMeal.apis.ABigData import GMBigData

gm = Flask(__name__)
api = flask_restful.Api(gm)

api.add_resource(GMUsers, "/group/meal/user/<string:users>")
api.add_resource(GMMeals, "/group/meal/meal/<string:meals>")
api.add_resource(GMMess, "/group/meal/mess/<string:mess>")
api.add_resource(GMCarts, "/group/meal/cart/<string:cart>")
api.add_resource(GMOrders, "/group/meal/order/<string:orders>")
api.add_resource(GMReview, "/group/meal/review/<string:review>")
api.add_resource(GMCoupons, "/group/meal/coupon/<string:card>")
api.add_resource(GMOther, "/group/meal/other/<string:other>")
api.add_resource(GMBigData, "/group/meal/data/<string:bigdata>")

'''
if __name__ == '__main__':
    gm.run('0.0.0.0', 443, debug=True, ssl_context=(
        "/etc/nginx/cert/1525609592348.pem"
    ))
'''
if __name__ == '__main__':
    gm.run('0.0.0.0', 7444, debug=True)
