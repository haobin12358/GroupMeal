# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from GroupMeal.config.response import APIS_WRONG

class GMBigData(Resource):
    def __init__(self):
        self.title = "=========={0}=========="
        from GroupMeal.control.CBigdata import CBigdata
        self.sbigdata = CBigdata()

    def get(self, bigdata):
        print(self.title.format(bigdata))

        apis = {
            "get_eat": "self.sbigdata.get_eat()"
        }

        if bigdata not in apis:
            return APIS_WRONG

        return eval(apis[bigdata])