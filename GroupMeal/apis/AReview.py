# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from GroupMeal.control.CReview import CReview
from GroupMeal.config.response import APIS_WRONG

class GMReview(Resource):
    def __init__(self):
        self.title = "=========={0}=========="
        self.control_review = CReview()

    def post(self, review):
        print(self.title.format(review))

        apis = {
            "create_review": "self.control_review.create_review()",
            "delete_user_review": "self.control_review.delete_user_review()"
        }

        if review in apis:
            return eval(apis[review])

        return APIS_WRONG

    def get(self, review):
        print(self.title.format(review))
        apis = {
            "get_review": "self.control_review.get_review()",
            "get_user_review": "self.control_review.get_user_review()",
            "get_product_review": "self.control_review.get_product_review()"
        }
        if review in apis:
            return eval(apis[review])

        return APIS_WRONG