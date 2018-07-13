# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import json
import uuid
from GroupMeal.config.response import SYSTEM_ERROR, PARAMS_MISS, PARAMS_REDUNDANCY
from GroupMeal.common.import_status import import_status
from GroupMeal.common.get_model_return_list import get_model_return_dict, get_model_return_list
from GroupMeal.common.MakeToken import token_to_usid
from GroupMeal.common.TransformToList import add_model

class CMeals():
    def __init__(self):
        self.title = "=========={0}=========="
        from GroupMeal.services.SUsers import SUsers
        self.susers = SUsers()
        from GroupMeal.services.SMeals import SMeals
        self.smeals = SMeals()
        # TODO 引用食堂

    def new_meal(self):
        args = request.args.to_dict()
        print(self.title.format("args"))
        print(args)
        print(self.title.format("args"))
        if "token" not in args and "MSid" not in args:
            return PARAMS_MISS
        USid = token_to_usid(args["token"])
        user = self.susers.get_user_by_usid(USid)
        if not user:
            return import_status("ERROR_NONE_USER", "GROUPMEAL_ERROR", "ERROR_NONE_USER")
        # TODO 食堂的存在验证
        data = request.data
        print(self.title.format("data"))
        print(data)
        print(self.title.format("data"))
        data = json.loads(data)

        meal_not_null_keys = ["MEname", "MEimage", "MEprice", "MEtype"]
        meal_null_keys = ["MEinfo", "MEdprice", "MEweight", "MEinventory", "MEprotein", "MEfat", "MEcarbohydrate",
                          "MEcalorie", "MEinorganic", "MEcalcium", "MEphosphorus", "MEiron"]

        for row in data.keys():
            if row not in meal_not_null_keys and row not in meal_null_keys:
                return PARAMS_REDUNDANCY

        data["MEvolume"] = 0
        data["MEfraction"] = 0
        data["MEstatus"] = 281
        data["MEtag"] = 296
        data["MSid"] = args["MSid"]
        data["MEid"] = str(uuid.uuid1())
        MEtype = data["MEtype"]
        data["MEtype"] =self.num_word_change(word=MEtype)

        print data
        new_meal = add_model("Meals", **data)
        print(self.title.format("new_meal"))
        print(new_meal)
        print(self.title.format("new_meal"))
        if not new_meal:
            return SYSTEM_ERROR

        return import_status("SUCCESS_ADD_MEAL", "OK")

    def num_word_change(self, num=None, word=None):
        num_word = [[200, "肉类"], [201, "特色餐饮"], [202, "套餐"], [203, "素食"],
                    [204, "汤菜"], [205, "面食"], [206, "粥点"], [207, "早餐"]]
        print num
        print(word)
        if num:
            for row in num_word:
                if row[0] == num:
                    return row[1]
        if word:
            for row in num_word:
                if row[1] == word.encode("utf8"):
                    return row[0]

    def tag_word_change(self, tag=None, word=None):
        tag_word = [[291, "热销"], [292, "活动商品"], [293, "推广商品"], [294, "广告商品"],
                    [295, "网红商品"], [296, "新品"]]
        if tag != None:
            for row in tag_word:
                if row[0] == tag:
                    return row[1]
        if word != None:
            for row in tag_word:
                if row[1] == word:
                    return row[0]

    def update_meal(self):
        args = request.args.to_dict()
        print(self.title.format("args"))
        print(args)
        print(self.title.format("args"))
        if "token" not in args and "MEid" not in args:
            return PARAMS_MISS
        USid = token_to_usid(args["token"])
        user = self.susers.get_user_by_usid(USid)
        if not user:
            return import_status("ERROR_NONE_USER", "GROUPMEAL_ERROR", "ERROR_NONE_USER")
        # TODO 食堂的存在验证
        data = request.data
        print(self.title.format("data"))
        print(data)
        print(self.title.format("data"))
        data = json.loads(data)

        meal_not_null_keys = ["MEname", "MEimage", "MEprice", "MEtype"]
        meal_null_keys = ["MEinfo", "MEdprice", "MEweight", "MEinventory", "MEprotein", "MEfat", "MEcarbohydrate",
                          "MEcalorie", "MEinorganic", "MEcalcium", "MEphosphorus", "MEiron"]

        for row in meal_not_null_keys:
            if row not in data.keys():
                return PARAMS_MISS
        for row in data.keys():
            if row not in meal_not_null_keys and row not in meal_null_keys:
                return PARAMS_REDUNDANCY
        if "MEtag" in data:
            data["MEtag"] = self.tag_word_change(word=data["MEtag"])
        if "MEtype" in data:
            data["MEtype"] = self.num_word_change(word=data["MEtype"])
        MEid = args["MEid"]

        update_meal = self.smeals.update_meal(MEid, data)
        print(self.title.format("update_meal"))
        print(update_meal)
        print(self.title.format("update_meal"))
        if not update_meal:
            return SYSTEM_ERROR

        return import_status("SUCCESS_UPDATE_MEAL", "OK")

    def shelf_or_obtained(self):
        args = request.args.to_dict()
        print(self.title.format("args"))
        print(args)
        print(self.title.format("args"))
        if "token" not in args and "MEid" not in args:
            return PARAMS_MISS
        USid = token_to_usid(args["token"])
        user = self.susers.get_user_by_usid(USid)
        if not user:
            return import_status("ERROR_NONE_USER", "GROUPMEAL_ERROR", "ERROR_NONE_USER")
        # TODO 食堂的存在验证
        data = request.data
        print(self.title.format("data"))
        print(data)
        print(self.title.format("data"))
        data = json.loads(data)

        meal_not_null_keys = ["MEname", "MEimage", "MEprice", "MEtype"]
        meal_null_keys = ["MEinfo", "MEdprice", "MEweight", "MEinventory", "MEprotein", "MEfat", "MEcarbohydrate",
                          "MEcalorie", "MEinorganic", "MEcalcium", "MEphosphorus", "MEiron"]

        for row in meal_not_null_keys:
            if row not in data.keys():
                return PARAMS_MISS
        for row in data.keys():
            if row not in meal_not_null_keys and row not in meal_null_keys:
                return PARAMS_REDUNDANCY
        if "MEtag" in data:
            data["MEtag"] = self.tag_word_change(word=data["MEtag"])
        if "MEtype" in data:
            data["MEtype"] = self.num_word_change(word=data["MEtype"])
        MEid = args["MEid"]

        update_meal = self.smeals.update_meal(MEid, data)
        print(self.title.format("update_meal"))
        print(update_meal)
        print(self.title.format("update_meal"))
        if not update_meal:
            return SYSTEM_ERROR

        return import_status("SUCCESS_UPDATE_MEAL", "OK")

    def meal_list(self):
        args = request.args.to_dict()
        print(self.title.format("args"))
        print(args)
        print(self.title.format("args"))
        if "MSid" not in args:
            return PARAMS_MISS
        if "MEtag" in args:
            args["MEtag"] = self.tag_word_change(word=args["MEtag"].encode("utf8"))
            meal_list = get_model_return_list(self.smeals.get_all_meal_by_msid_and_metag(args["MSid"], args["MEtag"]))
            print(self.title.format("meal_list"))
            print(meal_list)
            print(self.title.format("meal_list"))
        else:
            meal_list = get_model_return_list(self.smeals.get_all_meal_by_msid(args["MSid"]))
            print(self.title.format("meal_list"))
            print(meal_list)
            print(self.title.format("meal_list"))
        for meal in meal_list:
            meal["MEtype"] = self.num_word_change(num=meal["MEtype"])
            meal["MEtag"] = self.tag_word_change(tag=meal["MEtag"])
        response = import_status("SUCCESS_GET_MEAL", "OK")
        response["data"] = meal_list
        return response

    def meal_abo(self):
        args = request.args.to_dict()
        print(self.title.format("args"))
        print(args)
        print(self.title.format("args"))
        if "MEid" not in args:
            return PARAMS_MISS
        meal_abo = get_model_return_dict(self.smeals.get_meal_by_meid(args["MEid"]))
        print(self.title.format("meal_abo"))
        print(meal_abo)
        print(self.title.format("meal_abo"))
        meal_abo["MEtype"] = self.num_word_change(num=meal_abo["MEtype"])
        meal_abo["MEtag"] = self.tag_word_change(tag=meal_abo["MEtag"])
        response = import_status("SUCCESS_GET_MEAL", "OK")
        response["data"] = meal_abo
        return response

    def update_picture(self):
        return