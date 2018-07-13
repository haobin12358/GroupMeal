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

class CMess():
    def __init__(self):
        self.title = "=========={0}=========="
        from GroupMeal.services.SMess import SMess
        self.smess = SMess()
        from GroupMeal.services.SUsers import SUsers
        self.susers = SUsers()

    def get_mess_by_city(self):
        args = request.args.to_dict()
        print(self.title.format("args"))
        print(args)
        print(self.title.format("args"))
        if "MScity" not in args:
            return PARAMS_MISS
        mess_list = get_model_return_list(self.smess.get_mess_by_city(args["MScity"]))
        if not mess_list:
            return import_status("ERROR_NONE_MESS", "GROUPMEAL_ERROR", "ERROR_NONE_MESS")
        response = import_status("SUCCESS_GET_MESS", "OK")
        response["data"] = mess_list
        return response

    def get_mess_abo(self):
        args = request.args.to_dict()
        print(self.title.format("args"))
        print(args)
        print(self.title.format("args"))
        if "MSid" not in args:
            return PARAMS_MISS
        mess_list = get_model_return_dict(self.smess.get_mess_by_msid(args["MSid"]))
        if not mess_list:
            return SYSTEM_ERROR
        response = import_status("SUCCESS_GET_MESS", "OK")
        response["data"] = mess_list
        return response

    def new_mess(self):
        args = request.args.to_dict()
        print(self.title.format("args"))
        print(args)
        print(self.title.format("args"))
        if "token" not in args:
            return PARAMS_MISS
        USid = token_to_usid(args["token"])
        user = self.susers.get_user_by_usid(USid)
        if not user:
            return SYSTEM_ERROR
        # TODO 用户改管理员
        data = json.loads(request.data)
        print(self.title.format("data"))
        print(data)
        print(self.title.format("data"))
        mess_not_null_keys = ["MSname", "MSlocation", "MSimage", "MStelphone", "MScity"]
        mess_null_keys = ["MStimestart", "MStimeend", "MStrueimage", "MShealthimage", "MShealthlevel"]
        for key in mess_not_null_keys:
            if key not in data.keys():
                return PARAMS_MISS
        for key in data.keys():
            if key not in mess_not_null_keys and key not in mess_null_keys:
                return PARAMS_REDUNDANCY
        data["MSstatus"] = 501
        data["MSid"] = str(uuid.uuid1())
        new_mess = add_model("Mess", **data)
        print(self.title.format("new_mess"))
        print(new_mess)
        print(self.title.format("new_mess"))
        if not new_mess:
            return SYSTEM_ERROR
        return import_status("SUCCESS_NEW_MESS", "OK")

    def update_mess(self):
        args = request.args.to_dict()
        print(self.title.format("args"))
        print(args)
        print(self.title.format("args"))
        if "token" not in args or "MSid" not in args:
            return PARAMS_MISS
        USid = token_to_usid(args["token"])
        MSid = args["MSid"]
        user = self.susers.get_user_by_usid(USid)
        if not user:
            return SYSTEM_ERROR
        # TODO 用户改管理员
        mess = self.smess.get_mess_by_msid(MSid)
        if not mess:
            return SYSTEM_ERROR
        data = json.loads(request.data)
        print(self.title.format("data"))
        print(data)
        print(self.title.format("data"))
        mess_not_null_keys = ["MSname", "MSlocation", "MSimage", "MStelphone", "MScity"]
        mess_null_keys = ["MStimestart", "MStimeend", "MStrueimage", "MShealthimage", "MShealthlevel"]
        for key in mess_not_null_keys:
            if key not in data.keys():
                return PARAMS_MISS
        for key in data.keys():
            if key not in mess_not_null_keys and key not in mess_null_keys:
                return PARAMS_REDUNDANCY
        update_mess = self.smess.update_mess(MSid, data)
        print(self.title.format("update_mess"))
        print(update_mess)
        print(self.title.format("update_mess"))
        if not update_mess:
            return SYSTEM_ERROR
        return import_status("SUCCESS_UPDATE_MESS", "OK")

    def close_mess(self):
        return

    def get_all_city(self):
        sql_city = self.smess.get_all_city()
        all_city = {}.fromkeys(sql_city).keys()
        response = import_status("SUCCESS_GET_CITY", "OK")
        response["data"] = {}
        response["data"]["city"] = all_city
        return response
