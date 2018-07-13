# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from GroupMeal.config.response import APIS_WRONG
from GroupMeal.control.CMeals import CMeals

class GMMeals(Resource):
    def __init__(self):
        self.cmeals = CMeals()
        self.title = "==========={0}=========="

    def post(self, meals):
        print(self.title.format(meals))

        apis = {
            "new_meal":"self.cmeals.new_meal()",
            "update_meal":"self.cmeals.update_meal()",
            "shelf_or_obtained": "self.cmeals.shelf_or_obtained()",
            "update_picture": "self.cmeals.update_picture()"
        }

        if meals in apis:
            return eval(apis[meals])

        return APIS_WRONG

    def get(self, meals):
        print(self.title.format(meals))

        apis = {
            "meal_list":"self.cmeals.meal_list()",
            "meal_abo": "self.cmeals.meal_abo()"
        }

        if meals in apis:
            return eval(apis[meals])

        return APIS_WRONG