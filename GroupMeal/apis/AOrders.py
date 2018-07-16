# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource

from GroupMeal.config.response import APIS_WRONG

class GMOrders(Resource):
    def __init__(self):
        self.title = "=========={0}=========="
        from GroupMeal.control.COrders import COrders
        self.corders = COrders()

    def get(self, orders):
        print(self.title.format(orders))

        apis = {
            "get_order_list": "self.corders.get_order_list()",
            "get_order_abo": "self.corders.get_order_abo()"
        }

        if orders not in apis:
            return APIS_WRONG

        return eval(apis[orders])

    def post(self, orders):
        print(self.title.format(orders))

        apis = {
            "make_main_order": "self.corders.make_main_order()",
            "update_order_status": "self.corders.update_order_status()",
            "order_price": "self.corders.get_order_price()"
        }

        if orders not in apis:
            return APIS_WRONG

        return eval(apis[orders])