# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import datetime
from GroupMeal.config.response import SYSTEM_ERROR, PARAMS_MISS
from GroupMeal.common.import_status import import_status
from GroupMeal.common.get_model_return_list import get_model_return_dict, get_model_return_list
from GroupMeal.common.MakeToken import token_to_usid

class CBigdata():
    def __init__(self):
        from GroupMeal.services.SOrders import SOrders
        self.sorder = SOrders()
        from GroupMeal.services.SMeals import SMeals
        self.smeal = SMeals()
        self.title = '============{0}============'

    def get_eat(self):
        args = request.args.to_dict()
        print(self.title.format("args"))
        print(args)
        print(self.title.format("args"))
        if "token" not in args:
            return PARAMS_MISS
        USid = token_to_usid(args["token"])
        response_data = {
            "calorie": 0,
            "protein": 0,
            "fat": 0,
            "carbohydrate": 0,
            "inorganic": 0,
            "calcium": 0,
            "phosphorus": 0,
            "iron": 0
        }
        if "timedetail" in args:
            timedetail = int(args["timedetail"])
            time_now = datetime.datetime.now() + datetime.timedelta(days=timedetail)
            date = time_now.strftime("%Y%m%d%H%M%S")[0:8]
            time_start = date + "000000"
            time_end = date + "235959"
            all_order = get_model_return_list(self.sorder.get_all_order_by_time(time_start, time_end, USid))
            print(self.title.format("all_order"))
            print(all_order)
            print(self.title.format("all_order"))
            if not all_order:
                return SYSTEM_ERROR
            for order in all_order:
                OMid = order["OMid"]
                meal_list = get_model_return_list(self.sorder.get_order_item_by_oid(OMid))
                for meal in meal_list:
                    MEnumber = meal["MEnumber"]
                    MEid = meal["MEid"]
                    meal_abo = get_model_return_dict(self.smeal.get_meal_nutrition_by_meid(MEid))
                    response_data["calorie"] += meal_abo["MEcalorie"] * MEnumber
                    response_data["protein"] += meal_abo["MEprotein"] * MEnumber
                    response_data["fat"] += meal_abo["MEfat"] * MEnumber
                    response_data["carbohydrate"] += meal_abo["MEcarbohydrate"] * MEnumber
                    response_data["inorganic"] += meal_abo["MEinorganic"] * MEnumber
                    response_data["calcium"] += meal_abo["MEcalcium"] * MEnumber
                    response_data["phosphorus"] += meal_abo["MEphosphorus"] * MEnumber
                    response_data["iron"] += meal_abo["MEiron"] * MEnumber

        if "timestart" in args and "timeend" in args:
            return
        response = import_status("SUCCESS_GET_EAT", "OK")
        response["data"] = response_data
        return response



