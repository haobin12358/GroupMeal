# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import json
import uuid
from GroupMeal.common.lovebreakfast_error import dberror
from GroupMeal.common.TransformToList import add_model
from GroupMeal.config.response import SYSTEM_ERROR, PARAMS_MISS
from GroupMeal.common.import_status import import_status
from GroupMeal.common.MakeToken import token_to_usid
from GroupMeal.common.get_model_return_list import get_model_return_list, get_model_return_dict

class CCarts():
    def __init__(self):
        from GroupMeal.services.SCarts import SCarts
        self.scart = SCarts()
        from GroupMeal.services.SMeals import SMeals
        self.smeal = SMeals()
        from GroupMeal.services.SUsers import SUsers
        self.susers = SUsers()
        from GroupMeal.services.SMess import SMess
        self.smess = SMess()
        self.title = '============{0}============'

    def get_carts_by_uid(self):
        args = request.args.to_dict()
        print(self.title.format("args"))
        print(args)
        print(self.title.format("args"))
        if "token" not in args or "MSid" not in args:
            return PARAMS_MISS

        token = args.get("token")
        USid = token_to_usid(token)
        MSid = args["MSid"]
        is_user = self.susers.get_user_by_usid(USid)
        print(self.title.format("is_user"))
        print(is_user)
        print(self.title.format("is_user"))
        if not is_user:
            return import_status("ERROR_MESSAGE_NONE_USER", "GROUPMEAL_ERROR", "ERROR_CODE_NONE_USER")
        mess = self.smess.get_mess_by_msid(MSid)
        if not mess:
            return SYSTEM_ERROR
        cart_list = get_model_return_list(self.scart.get_carts_by_Uid(USid))
        print(self.title.format("cartlist"))
        print(cart_list)
        print(self.title.format("cartlist"))

        i = len(cart_list) - 1
        while i >= 0:
            MEid = cart_list[i]["MEid"]
            msid = self.smeal.get_msid_by_meid(MEid)
            print(self.title.format("msid"))
            print(msid)
            print(self.title.format("msid"))
            if msid != MSid:
                cart_list.remove(cart_list[i])
            else:
                meal = get_model_return_dict(self.smeal.get_meal_by_meid(MEid))
                print(self.title.format("meal"))
                print(meal)
                print(self.title.format("meal"))
                if not meal:
                    return SYSTEM_ERROR
                for key in meal.keys():
                    cart_list[i][key] = meal[key]
            i = i - 1

        back_response = import_status("SUCCESS_GET_MESSAGE", "OK")
        back_response["data"] = cart_list
        return back_response

    def add_or_update_cart(self):
        args = request.args.to_dict()
        print(self.title.format("args"))
        print(args)
        print(self.title.format("args"))
        data = json.loads(request.data)
        print(self.title.format("data"))
        print(data)
        print(self.title.format("data"))

        if "token" not in args:
            return PARAMS_MISS
        token = args.get("token")
        USid = token_to_usid(token)
        MEid = data["MEid"]
        CAnumber = data["CAnumber"]
        if CAnumber <= 0:
            PBnumber = self.scart.get_canumber_by_meid_and_usid(MEid, USid)
            pnum = int(CAnumber) + int(PBnumber)
            if pnum <= 0:
                return self.del_cart(USid, MEid)
            else:
                cart = self.scart.get_cart_by_usid_meid(USid, MEid)
                print(self.title.format("cart"))
                print(cart)
                print(self.title.format("cart"))
                if not cart:
                    return SYSTEM_ERROR
                self.scart.update_num_cart(pnum, cart.CAid)
        try:
            if not self.smeal.get_meal_by_meid(MEid):
                return import_status("ERROR_MESSAGE_NONE_PRODUCT", "GROUPMEAL_ERROR", "ERROR_NONE_PRODUCT")
            cart = self.scart.get_cart_by_usid_meid(USid, MEid)
            print(self.title.format("cart"))
            print(cart)
            print(self.title.format("cart"))
            if cart:
                PBnumber = self.scart.get_canumber_by_meid_and_usid(MEid, USid)
                pnum = int(CAnumber) + int(PBnumber)
                self.scart.update_num_cart(pnum, cart.CAid)
            else:
                add_model("Cart",
                          **{
                              "CAid": str(uuid.uuid1()),
                              "CAnumber": CAnumber,
                              "USid": USid,
                              "MEid": MEid
                          })
        except dberror:
            return SYSTEM_ERROR
        except Exception as e:
            print(e.message)
            return SYSTEM_ERROR

        return import_status("SUCCESS_MESSAGE_UPDATE_CART", "OK")

    def del_cart(self, uid, pid):
        try:
            cart = self.scart.get_cart_by_usid_meid(uid, pid)
            print(self.title.format("cart"))
            print(cart)
            print(self.title.format("cart"))
            if not cart:
                return import_status("ERROR_MESSAGE_NONE_PRODUCT", "GROUPMEAL_ERROR", "ERROR_NONE_PRODUCT")
            self.scart.del_carts(cart.CAid)
            return import_status("SUCCESS_MESSAGE_DEL_CART", "OK")
        except Exception as e:
            print(e.message)
            return SYSTEM_ERROR

    def del_product(self):
        args = request.args.to_dict()
        print(self.title.format("args"))
        print(args)
        print(self.title.format("args"))
        if "token" not in args:
            return PARAMS_MISS
        data = json.loads(request.data)
        print(self.title.format("data"))
        print(data)
        print(self.title.format("data"))

        if "PRid" not in data:
            return PARAMS_MISS
        token = args.get("token")
        uid = token_to_usid(token)
        return self.del_cart(uid, data.get("PRid"))
