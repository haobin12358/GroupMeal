# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import json
from GroupMeal.config.response import SYSTEM_ERROR, PARAMS_MISS, PARAMS_REDUNDANCY
import datetime
from GroupMeal.common import timeformate
from GroupMeal.common.import_status import import_status
from GroupMeal.common.get_model_return_list import get_model_return_list, get_model_return_dict
from GroupMeal.common.get_str import get_str
from GroupMeal.common.MakeToken import token_to_usid
from GroupMeal.common.TransformToList import add_model


class COrders():

    def __init__(self):
        self.title = "=========={0}=========="
        from GroupMeal.services.SUsers import SUsers
        self.susers = SUsers()
        from GroupMeal.services.SOrders import SOrders
        self.sorders = SOrders()
        from GroupMeal.services.SCarts import SCarts
        self.scart = SCarts()
        from GroupMeal.services.SMeals import SMeals
        self.smeal = SMeals()
        from GroupMeal.services.SMess import SMess
        self.smess = SMess()
        global OMstatus_list
        OMstatus_list = ("已取消", "未支付", "已支付", "已接单", "已配送", "已装箱", "已完成", "已评价")

    def get_order_list(self):
        args = request.args.to_dict()
        if "token" not in args:
            return PARAMS_MISS

        print(self.title.format("args"))
        print(args)
        print(self.title.format("args"))

        token = args.get("token")
        Uid = token_to_usid(token)
        user = self.susers.get_user_by_usid(Uid)
        if not user:
            return SYSTEM_ERROR
        order_list = get_model_return_list(self.sorders.get_all_order_by_uid(Uid))
        print(self.title.format("order_list"))
        print(order_list)
        print(self.title.format("order_list"))

        if order_list:
            for order in order_list:
                if int(order["OMstatus"]) >= 305 and int(order["OMstatus"]) <= 310:
                    order["is_index"] = 702
                else:
                    order["is_index"] = 701
                order["OMstatus"] = self.status_num_change(num=order["OMstatus"])
                order["OMtime"] = timeformate.get_web_time_str(str(order["OMtime"]))

                order_items = get_model_return_list(self.sorders.get_order_item_by_oid(order["OMid"]))
                print(self.title.format("order_items"))
                print(order_items)
                print(self.title.format("order_items"))
                order["Orderitems"] = []
                for raw in order_items:
                    MEid = raw["MEid"]
                    meal = get_model_return_dict(self.smeal.get_meal_by_meid(MEid))
                    print(self.title.format("product"))
                    print(meal)
                    print(self.title.format("product"))
                    raw.update(meal)
                    order["Orderitems"].append(raw)

        response_make_main_order = import_status("SUCCESS_GET_ORDER", "OK")
        response_make_main_order["data"] = order_list

        return response_make_main_order

    def get_order_abo(self):
        args = request.args.to_dict()
        if "token" not in args or "OMid" not in args:
            return PARAMS_MISS

        print(self.title.format("args"))
        print(args)
        print(self.title.format("args"))
        Oid = args["OMid"]
        token = args.get("token")
        Uid = token_to_usid(token)
        user = self.susers.get_user_by_usid(Uid)
        if not user:
            return SYSTEM_ERROR
        order_abo = get_model_return_dict(self.sorders.get_order_abo_by_oid(Oid))
        print(self.title.format("order_abo"))
        print(order_abo)
        print(self.title.format("order_abo"))
        order_abo["OMtime"] = timeformate.get_web_time_str(order_abo["OMtime"])
        order_abo["is_index"] = 701
        if int(order_abo["OMstatus"]) >= 305 and int(order_abo["OMstatus"]) <= 310:
            order_abo["is_index"] = 702
        order_abo["OMstatus"] = self.status_num_change(num=order_abo["OMstatus"])
        # TODO 优惠券解析CPid

        users = get_model_return_dict(self.susers.get_uname_utel_by_uid(Uid))
        print(self.title.format("users"))
        print(users)
        print(self.title.format("users"))
        order_abo.update(users)
        order_items = get_model_return_list(self.sorders.get_order_item_by_oid(Oid))
        print(self.title.format("order_items"))
        print(order_items)
        print(self.title.format("order_items"))

        order_abo["Orderitems"] = order_items
        for row in order_items:
            product = get_model_return_dict(self.smeal.get_meal_by_meid(row["MEid"]))
            print(self.title.format("product"))
            print(product)
            print(self.title.format("product"))
            row.update(product)

        response_make_main_order = import_status("SUCCESS_GET_ORDER", "OK")
        response_make_main_order["data"] = order_abo
        return response_make_main_order

    def make_main_order(self):
        args = request.args.to_dict()
        data = request.data
        data = json.loads(data)
        print(self.title.format("args"))
        print(args)
        print(self.title.format("args"))
        print(self.title.format("data"))
        print(data)
        print(self.title.format("data"))

        if "token" not in args or "MSid" not in args:
            return PARAMS_MISS

        params_list = ["Order_items", "OMtotal", "OMtime"]
        for params in params_list:
            if params not in data:
                return PARAMS_MISS
        null_params = ["OMabo", "CPid"]
        for params in data.keys():
            if params not in null_params and params not in params_list:
                return PARAMS_REDUNDANCY

        token = args.get("token")
        Uid = token_to_usid(token)
        user = self.susers.get_user_by_usid(Uid)
        if not user:
            return SYSTEM_ERROR
        MSid = args["MSid"]
        OMtime = timeformate.get_db_time_str(data["OMtime"])

        order_item = data["Order_items"]
        OMcode = self.make_code()
        import uuid
        OMid = str(uuid.uuid1())
        try:
            for op in order_item:
                MEstatus = self.smeal.get_mestatus_by_meid(op["MEid"])
                print(self.title.format("MEstatus"))
                print(MEstatus)
                print(self.title.format("MEstatus"))
                if MEstatus != 281:
                    return import_status("error_no_pro", "GROUPMEAL_ERROR", "error_no_pro")
                msid = self.smeal.get_msid_by_meid(op["MEid"])
                if msid != MSid:
                    return import_status("ERROR_MEAL_IN_MESS", "GROUPMEAL_ERROR", "ERROR_MEAL_IN_MESS")
                add_model("OrderPart", **{
                    "OPid": str(uuid.uuid1()),
                    "OMid": OMid,
                    "MEid": op["MEid"],
                    "MEnumber": op["MEnumber"]
                })
                volume = self.smeal.get_mevolume_by_meid(op["MEid"])
                volume = volume + 1
                update_meal = self.smeal.update_meal(op["MEid"], {"MEvolume": volume})
                if not update_meal:
                    return SYSTEM_ERROR

                cart = get_model_return_dict(
                    self.scart.get_cart_by_usid_meid(Uid, op["MEid"]))
                print(self.title.format("cartt"))
                print(cart)
                print(self.title.format("cartt"))
                self.scart.del_carts(cart.get("CAid"))

            print(self.title.format("success add orderpart"))
            # TODO 增加优惠券id
            self.sorders.add_model("OrderMain", **{
                "OMid": OMid,
                "OMtime": OMtime,
                "OMstatus": 301,
                "USid": Uid,
                "OMcode": OMcode,
                "OMabo": data["OMabo"],
                "OMtotal": data["OMtotal"]
            })

            # self.scoupons.update_carbackage(get_str(data, "CAid"))
            response_make_main_order = import_status("SUCCESS_MAKE_ORDER", "OK")
            response_make_main_order["data"] = {}
            response_make_main_order["data"]["OMid"] = OMid
            return response_make_main_order
        except Exception as e:
            print(self.title.format("error"))
            print(e.message)
            print(self.title.format("error"))
            return SYSTEM_ERROR

    def status_num_change(self, status=None, num=None):
        status_num = [[301, "未支付"], [302, "支付中"], [303, "已支付"], [304, "待取餐"], [305, "已取餐"],
                    [306, "已评价"], [307, "退款中"], [308, "已退款"], [309, "已取消"], [310, "申请退款"]]
        if num != None:
            for row in status_num:
                if row[0] == num:
                    return row[1]
        if status != None:
            for row in status_num:
                if row[1] == status:
                    return row[0]

    def update_order_status(self):
        args = request.args.to_dict()
        data = request.data
        data = json.loads(data)

        if "token" not in args:
            return PARAMS_MISS
        if "OMstatus" not in data or "OMid" not in data:
            return PARAMS_MISS
        # 处理token过程，这里未设计
        token = args.get("token")
        USid = token_to_usid(token)
        user = self.susers.get_user_by_usid(USid)
        if not user:
            return SYSTEM_ERROR

        OMstatus = self.status_num_change(status=data["OMstatus"].encode("utf8"))
        if not OMstatus:
            return import_status("ERROR_UNKNOWN_OMSTATUS", "GROUPMEAL_ERROR", "ERROR_UNKNOWN_OMSTATUS")

        OMid = data["OMid"]
        usid = self.sorders.get_usid_by_omid(OMid)
        if USid != usid:
            return import_status("ERROR_NONE_PERMISSION", "GROUPMEAL_ERROR", "ERROR_NONE_PERMISSION")

        update_OMstatus = {}
        update_OMstatus["OMstatus"] = OMstatus

        response_update_order_status = self.sorders.update_order_by_oid(OMid, update_OMstatus)

        if not response_update_order_status:
            return SYSTEM_ERROR

        return import_status("SUCCESS_UPDATE_ORDER", "OK")

    def checktime(self):
        """
        check now is between 6:00 and 22:00
        :return:
        """
        timenow = datetime.datetime.now()

        if 6 < timenow.hour < 22:
            return False
        return True

    def make_code(self):
        import random
        while True:
            randomcode = random.randint(100000, 999999)
            order = self.sorders.get_order_main_by_code(randomcode)
            if not order:
                return randomcode

    def get_order_price(self):
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
        meals_list = data.get("meallist")
        order_list = []
        OMprice = 0
        try:
            for meal in meals_list:
                MEnumber = meal.get("MEnumber")
                meal_abo = get_model_return_dict(self.smeal.get_meal_by_meid(meal.get("MEid")))
                if not meal_abo["MEdprice"]:
                    MEprice = meal_abo["MEdprice"]
                else:
                    MEprice = meal_abo["MEprice"]
                OMprice += (MEprice * MEnumber)
                order_list.append(meal)
            # TODO 优惠券计算过程
            """
            if "COid" in data and get_str(data, "COid"):
                coupon = get_model_return_dict(self.scoupons.get_coupons_by_couid(get_str(data, "COid")))
                print(self.title.format(coupon))
                print(coupon)
                print(self.title.format(coupon))
                OMprice = self.compute_om_price_by_coupons(coupon, OMprice)
                if not isinstance(OMprice, float):
                    return OMprice
            """
            print(self.title.format("OMprice"))
            print(OMprice)
            print(self.title.format("OMprice"))

            data = import_status("SUCCESS_MESSAGE_GET_INFO", "OK")
            data["data"] = {"OMprice": OMprice, "meallist": order_list}
            return data
        except Exception as e:
            print(self.title.format("get order error"))
            print(e.message)
            print(self.title.format("get order error"))

    def compute_om_price_by_coupons(self, coupon, omprice):
        from decimal import Decimal
        time_now = timeformate.get_db_time_str()
        omprice = Decimal(str(omprice))
        print(self.title.format("timenow"))
        print(time_now)
        print(self.title.format("timenow"))
        print(self.title.format("coutime"))
        print("endtime:", coupon.get("COend", ""), "\n starttime:", coupon.get("COstart", ""))
        print(self.title.format("coutime"))

        if coupon.get("COend") and time_now > coupon.get("COend"):
            return import_status("ERROR_MESSAGE_COUPONS_TIMEEND", "SHARPGOODS_ERROR", "ERROR_TIMR")

        if coupon.get("COstart") and time_now < coupon.get("COstart"):
            return import_status("ERROR_MESSAGE_COUPONS_TIMESTART", "SHARPGOODS_ERROR", "ERROR_TIMR")

        if omprice > coupon.get("COfilter", 0):
            if coupon.get("COamount"):
                omprice = omprice - Decimal(str(coupon.get("COamount", 0)))
            elif isinstance(coupon.get("COdiscount"), float):
                omprice = omprice * Decimal(str(coupon.get("COdiscount")))
            else:
                # 优惠券不打折扣也不满减，要他干嘛
                pass

        print(self.title.format("限定两位小数前的omproce"))
        print(omprice)
        print(self.title.format("限定两位小数前的omproce"))
        omprice = omprice.quantize(Decimal("0.00"))
        return float(omprice) if omprice >= 0 else 0.00

    def check_order_date(self, order_date):
        timenow = datetime.datetime.date()
        time_order = datetime.datetime.strptime(order_date, timeformate.format_forweb_no_second).date()

        if timenow >= time_order:
            return False
        return True


if __name__ == "__main__":
    sorder = COrders()
"""
{
    "status": 200,
    "message": "获取区域信息成功",
    "data": [
        {
            "ACid": "f9490b5d-1745-47e9-b399-36614a8e10e4",
            "ACname": "杭州市",
            "AFtype: ["地铁","生活区"]
        }
    ]
}
"""