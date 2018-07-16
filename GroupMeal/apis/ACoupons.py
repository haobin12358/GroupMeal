# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from GroupMeal.control.CCoupons import CCoupons
from GroupMeal.config.response import APIS_WRONG

class LBCoupons(Resource):

    def __init__(self):
        self.title = "=========={0}=========="
        self.coupon = CCoupons()

    def post(self, card):
        print(self.title.format(card))

        apis = {
            "update_coupons": "self.coupon.add_cardpackage()",
        }

        if card in apis:
            return eval(apis[card])

        return APIS_WRONG

    def get(self, card):
        print(self.title.format(card))

        apis = {
            "get_cardpkg": "self.coupon.get_cart_pkg()"

        }

        if card in apis:
            return eval(apis[card])

        return APIS_WRONG
