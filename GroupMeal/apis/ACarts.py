# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from GroupMeal.control.CCarts import CCarts
from GroupMeal.config.response import APIS_WRONG

class GMCarts(Resource):
    def __init__(self):
        self.ccart = CCarts()
        self.title = "=========={0}=========="

    def post(self, cart):
        print(self.title.format(cart))

        apis = {
            "update": "self.ccart.add_or_update_cart()"
        }

        if cart in apis:
            return eval(apis[cart])

        return APIS_WRONG

    def get(self, cart):
        print(self.title.format(cart))

        apis = {
            "get_all": "self.ccart.get_carts_by_uid()"
        }

        if cart in apis:
            return eval(apis[cart])

        return APIS_WRONG
