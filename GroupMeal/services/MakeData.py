# *- coding:utf8 *-
import sys
import os
args = sys.argv
path = os.getcwd()
if len(args) > 1:
    path = args[1]  # /opt/LoveBreakfast
print(path)
sys.path.append(os.path.dirname(path))  # 增加系统路径
from common.TransformToList import add_model
import uuid


class MakeData():
    def __init__(self):
        from services.SUsers import SUsers
        self.users = SUsers()
        from services.SCoupons import SCoupons
        self.scoupons = SCoupons()

    def setUid(self):
        uid = str(uuid.uuid4())
        return uid

    def add_user(self, uid):
        try:
            add_model("Users",
                      **{
                          "USid": uid,
                          "UStelphone": "17706441101",
                          "USpassword": "123",
                          "USname": "测试账号",
                          "USsex": 101,
                          "UScoin": 100.1,
                          "USinvatecode": "ETECH007"
                      })
        except Exception as e:
            print e.message

    def setCOid(self):
        list_coid = []
        list_coid.append(str(uuid.uuid4()))
        list_coid.append(str(uuid.uuid4()))
        list_coid.append(str(uuid.uuid4()))
        return list_coid

    def add_coupons(self, coid):
        try:
            for row in coid:
                add_model("Coupons",
                          **{
                              "COid": row,
                              "COfilter": 20,
                              "COdiscount": 1,
                              "COamount": None,
                              "COstart": None,
                              "COend": None
                          })
        except Exception as e:
            print e.message

    def add_cardpackage(self, coid, uid):
        try:
            add_model("Cardpackage",
                      **{
                          "CAid": str(uuid.uuid4()),
                          "USid": uid,
                          "COid": coid[0],
                          "CAstatus": 1,
                          "CAstart": "20180423000000",
                          "CAend": "20180429000000"
                      })
            add_model("Cardpackage",
                      **{
                          "CAid": str(uuid.uuid4()),
                          "USid": uid,
                          "COid": coid[1],
                          "CAstatus": 2,
                          "CAstart": "20180429000000",
                          "CAend": "20180522000000"
                      })
            add_model("Cardpackage",
                      **{
                          "CAid": str(uuid.uuid4()),
                          "USid": uid,
                          "COid": coid[2],
                          "CAstatus": 2,
                          "CAstart": "20180329000000",
                          "CAend": "20180419000000"
                      })
        except Exception as e:
            print e.message

    def set_pid(self):
        pid_list = []
        pid_list.append(str(uuid.uuid4()))
        pid_list.append(str(uuid.uuid4()))
        pid_list.append(str(uuid.uuid4()))
        pid_list.append(str(uuid.uuid4()))
        pid_list.append(str(uuid.uuid4()))
        return pid_list

    def add_product(self, pid):
        try:
            add_model("Products",
                      **{
                          "PRid": pid[0],
                          "PRname": "测试套餐1",
                          "PRprice": 28.88,
                          "PRstatus": 1,
                          "PRimage": "http://120.79.182.43:7444/imgs/hello.jpg",
                          "PRinfo": "测试数据",
                          "PRsalesvolume": 100,
                          "PRscore": 4.2
                      })
            add_model("Products",
                      **{
                          "PRid": pid[1],
                          "PRname": "测试套餐2",
                          "PRprice": 18.88,
                          "PRstatus": 1,
                          "PRimage": "http://120.79.182.43:7444/imgs/hello.jpg",
                          "PRinfo": "测试数据",
                          "PRsalesvolume": 300,
                          "PRscore": 3.2
                      })
            add_model("Products",
                      **{
                          "PRid": pid[2],
                          "PRname": "测试套餐3",
                          "PRprice": 9.88,
                          "PRstatus": 1,
                          "PRimage": "http://120.79.182.43:7444/imgs/hello.jpg",
                          "PRinfo": "测试数据",
                          "PRsalesvolume": 120,
                          "PRscore": 3.5
                      })
            add_model("Products",
                      **{
                          "PRid": pid[3],
                          "PRname": "测试套餐4",
                          "PRprice": 15.88,
                          "PRstatus": 1,
                          "PRimage": "http://120.79.182.43:7444/imgs/hello.jpg",
                          "PRinfo": "测试数据",
                          "PRsalesvolume": 1001,
                          "PRscore": 2.1
                      })
            add_model("Products",
                      **{
                          "PRid": pid[4],
                          "PRname": "测试套餐5",
                          "PRprice": 13.88,
                          "PRstatus": 1,
                          "PRimage": "http://120.79.182.43:7444/imgs/hello.jpg",
                          "PRinfo": "测试数据",
                          "PRsalesvolume": 5,
                          "PRscore": 1.6
                      })
        except Exception as e:
            print e.message

    def add_machinery(self, pridlist, aaidlist):
        for aaid in aaidlist:
            for prid in pridlist:
                add_model("Machinery", **{
                    "MAid": str(uuid.uuid1()),
                    "AAid": aaid,
                    "PRid": prid
                })

    def add_city(self, acid):
        add_model("AddCity",
                  **{
                      "ACid": acid,
                      "ACname": "杭州市"
                  })

    def add_addfirst(self, acid):
        afidlist = []
        addfirst = [
            {"name": "萧山区", "aftype": 1},
            {"name": "下沙区", "aftype": 1},
            {"name": "上城区", "aftype": 1},
            {"name": "下城区", "aftype": 1},
            {"name": "滨江区", "aftype": 1},
            {"name": "地铁1号线", "aftype": 0},
            {"name": "地铁2号线", "aftype": 0},
            {"name": "地铁4号线", "aftype": 0},
        ]
        for data in addfirst:
            afid = str(uuid.uuid4())
            add_model("AddressFirst",
                      **{
                          "AFid": afid,
                          "ACid": acid,
                          "AFtype": data["aftype"],
                          "AFname": data["name"],
                      })
            afidlist.append(afid)
        return afidlist

    def add_addsecond(self, afid):
        asidlist = []
        asnamelist = []
        addsecond = [
            ["滨盛创业园", "潮锦创业园", "江拓创业园"],
            ["创巢创业园", "下沙网", "浙江省海外留学人员创业园"],
            ["科技创业中心"],
            ["创意园区", "嘉得威创业园", "网络文学创业园"],
            ["江虹国际创业园", "万恒创业园", "京安创业园"],
            ["打铁关", "西兴", "龙翔桥", "江陵路"],
            ["白洋", "三墩", "文新", "沈塘桥"],
            ["新风", "市民中心", "南星桥", "复兴路"],
        ]
        for index, data in enumerate(afid):
            for asname in addsecond[index]:
                asid = str(uuid.uuid4())
                add_model("AddressSecond",
                          **{
                              "ASid": asid,
                              "AFid": data,
                              "ASname": asname
                          })
                asidlist.append(asid)
                asnamelist.append(asname)
        return asidlist, asnamelist

    def add_addabo(self, asidlist, asnamelist):
        aaid_list = []
        for index, i in enumerate(asidlist):
            aaid = str(uuid.uuid4())
            add_model("AddressAbo",
                      **{
                          "AAid": aaid,
                          "ASid": i,
                          "AAmessage": asnamelist[index] + "A区拐角机器",
                          "AAimage": "图片地址",
                      })
            aaid_list.append(aaid)
        return aaid_list


if __name__ == "__main__":
    # pass
    makedata = MakeData()
    acid = makedata.setUid()
    makedata.add_city(acid)
    afid = makedata.add_addfirst(acid)
    asid, asname = makedata.add_addsecond(afid)
    aaid = makedata.add_addabo(asid, asname)

    uid = makedata.setUid()
    pid = makedata.set_pid()
    coid = makedata.setCOid()

    makedata.add_user(uid)
    makedata.add_coupons(coid)
    makedata.add_cardpackage(coid, uid)
    makedata.add_product(pid)
    makedata.add_machinery(pid, aaid)
