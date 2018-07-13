# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from GroupMeal.control.CUsers import CUsers
from GroupMeal.config.response import APIS_WRONG

class GMUsers(Resource):
    def __init__(self):
        self.cusers = CUsers()
        self.title = "==========={0}=========="

    def post(self, users):
        print(self.title.format(users))

        apis = {
            "register":"self.cusers.register()",
            "login":"self.cusers.login()",
            "update_info":"self.cusers.update_info()",
            "update_pwd":"self.cusers.update_pwd()",
            "get_inforcode":"self.cusers.get_inforcode()",
            "forget_pwd": "self.cusers.forget_pwd()",
            "update_first_user": "self.cusers.update_first_user()"
        }

        if users in apis:
            return eval(apis[users])

        return APIS_WRONG

    def get(self, users):
        print(self.title.format(users))

        apis = {
            "all_info":"self.cusers.all_info()",
            "get_first_user": "self.cusers.get_first_user()"
        }

        if users in apis:
            return eval(apis[users])

        return APIS_WRONG