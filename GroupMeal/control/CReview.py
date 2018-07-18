# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import uuid
import json
from GroupMeal.services.SMeals import SMeals
from GroupMeal.common.get_str import get_str
from GroupMeal.common.import_status import import_status
from GroupMeal.services.SReview import SReview
from GroupMeal.control.COrders import COrders
from GroupMeal.services.SUsers import SUsers
from GroupMeal.services.SOrders import SOrders
from GroupMeal.config.response import PARAMS_MISS, SYSTEM_ERROR
from GroupMeal.common.TransformToList import add_model
from GroupMeal.common.get_model_return_list import get_model_return_dict, get_model_return_list
from GroupMeal.common.MakeToken import token_to_usid

class CReview():
    def __init__(self):
        self.smeal = SMeals()
        self.service_review = SReview()
        self.control_order = COrders()
        self.service_user = SUsers()
        self.service_order = SOrders()
        self.title = '============{0}============'

    def create_review(self):
        args = request.args.to_dict()
        print(self.title.format("args"))
        print(args)
        print(self.title.format("args"))
        if "token" not in args.keys() or "OMid" not in args.keys():
            return PARAMS_MISS

        token = args.get("token")
        USid = token_to_usid(token)
        OMid = get_str(args, "OMid")
        OMstatus = self.service_order.get_omstatus_by_omid(OMid)
        if OMstatus != 305:
            return import_status("ERROR_MESSAGE_WRONG_OMSTATUS", "GROUPMEAL_ERROR", "ERROR_CODE_WRONG_OMSTATUS")

        data = request.data
        data = json.loads(data)
        print(self.title.format("data"))
        print(data)
        print(self.title.format("data"))

        for row in data:
            print(self.title.format("data_item"))
            print(row)
            print(self.title.format("data_item"))
            if "MEid" not in row or "REscore" not in row or "REfscore" not in row:
                return PARAMS_MISS
            if "REcontent" in row:
                REcontent = row["REcontent"]
            else:
                REcontent = None
            PRid = row["MEid"]
            REscore = row["REscore"]
            print(self.title.format("REscore"))
            print(REscore)
            print(self.title.format("REscore"))
            try:
                add_model("Review",
                          **{
                              "REid": str(uuid.uuid1()),
                              "OMid": OMid,
                              "MEid": PRid,
                              "REscore": REscore,
                              "REcontent": REcontent,
                              "REfscore": row["REfscore"]
                          })
            except Exception as e:
                print(self.title.format("add_review"))
                print(e.message)
                print(self.title.format("add_review"))
                return SYSTEM_ERROR

            product_volue = self.smeal.get_mevolume_by_meid(PRid)
            product_score = self.smeal.get_mefrac_by_meid(PRid)

            score = (product_score * product_volue + REscore)/product_volue
            product = {
                "MEfraction": score
            }
            update_product = self.smeal.update_meal(PRid, product)
            print(self.title.format("update_product"))
            print(update_product)
            print(self.title.format("update_product"))
            if not update_product:
                return SYSTEM_ERROR

            order = {
                "OMstatus": 306
            }
            update_order = self.service_order.update_order_by_oid(OMid, order)
            print(self.title.format("update_order"))
            print(update_order)
            print(self.title.format("update_order"))
            if not update_order:
                return SYSTEM_ERROR

        back_response = import_status("SUCCESS_MESSAGE_ADD_REVIEW", "OK")
        return back_response

    def get_review(self):
        args = request.args.to_dict()
        print(self.title.format("args"))
        print(args)
        print(self.title.format("args"))

        if "OMid" not in args.keys() or "token" not in args.keys():
            return PARAMS_MISS

        token = args.get("token")
        USid = token_to_usid(token)
        # TODO USid的作用？

        OMid = get_str(args, "OMid")

        all_review = get_model_return_list(self.service_review.get_review(OMid))
        print(self.title.format("all_review"))
        print(all_review)
        print(self.title.format("all_review"))
        if not all_review:
            return SYSTEM_ERROR

        for row in all_review:
            product = get_model_return_dict(self.smeal.get_meal_by_meid(row.get("MEid")))
            print(self.title.format("product"))
            print(product)
            print(self.title.format("product"))
            if not product:
                return SYSTEM_ERROR
            row.update(product)

        back_response = import_status("SUCCESS_MESSAGE_ADD_REVIEW", "OK")
        back_response["data"] = all_review
        return back_response

    def delete_user_review(self):
        args = request.args.to_dict()  # 捕获前端的URL参数，以字典形式呈现
        # 判断url参数是否异常
        if len(args) != 1 or "Uid" not in args.keys() or "Rid" not in args.keys():
            message, status, statuscode = import_status("URL_PARAM_WRONG", "response_error", "URL_PARAM_WRONG")
            return {
                "message": message,
                "status": status,
                "statuscode": statuscode,
            }
        uid_to_str = get_str(args, "Uid")
        uid_list = []
        if uid_to_str not in uid_list:
            message, status, statuscode = import_status("URL_PARAM_WRONG", "response_error", "URL_PARAM_WRONG")
            return {
                "message": message,
                "status": status,
                "statuscode": statuscode,
            }
        rid_to_str = get_str(args, "Rid")
        rid_list = self.service_review.get_rid_by_uid(uid_to_str)
        if rid_to_str not in rid_list:
            message, status, statuscode = import_status("NO_THIS_REVIEW", "response_error", "NO_THIS_REVIEW")
            return {
                "message": message,
                "status": status,
                "statuscode": statuscode,
            }
        result = self.service_review.delete_user_review(rid_to_str)
        print(result)
        return {
            "message": "delete review success !",
            "status": 200,
        }