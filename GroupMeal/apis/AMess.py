# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from GroupMeal.config.response import APIS_WRONG
from GroupMeal.control.CMess import CMess

class GMMess(Resource):
    def __init__(self):
        self.cmess = CMess()
        self.title = "==========={0}=========="

    def get(self, mess):
        print(self.title.format(mess))

        apis = {
            "get_mess_by_city": "self.cmess.get_mess_by_city()",
            "get_mess_abo": "self.cmess.get_mess_abo()",
            "get_all_city": "self.cmess.get_all_city()"
        }
        if mess in apis:
            return eval(apis[mess])
        return APIS_WRONG

    def post(self, mess):
        print(self.title.format(mess))

        apis = {
            "new_mess": "self.cmess.new_mess()",
            "update_mess": "self.cmess.update_mess()",
            "close_mess": "self.cmess.close_mess()"
        }
        if mess in apis:
            return eval(apis[mess])
        return APIS_WRONG