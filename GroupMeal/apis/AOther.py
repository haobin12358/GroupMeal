# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource, request
from GroupMeal.config.response import PARAMS_MISS
from GroupMeal.common.import_status import import_status
from GroupMeal.config.response import SYSTEM_ERROR
import datetime

class GMOther(Resource):
    def __init__(self):
        from GroupMeal.services.SOrders import SOrders
        self.sorders = SOrders()
        self.title = '============{0}============'

    def get(self, other):
        if other == "disclaimer":
            return """欢迎您使用网上购物。请您务必先仔细阅读本用户协议（包括隐私权条款及法律条款），我们将按以下的方式和条件为您提供我们的服务。如果您使用我们的服务，即表示您完全同意并接受本用户协议。 
              
                    尊敬的买家朋友，请在购买本店产品之前，一定要花几分钟认真阅读以下内容以避免我们的交易发生一些不必要的误会。

                    为了节省您宝贵的时间，请一次性问完或者多问一些您需要咨询的问题，因为同时在线咨询客户较多，我们是先来先回复，再接待下一个客户可能得好几分钟或者几十分钟才能再回复您的第二条消息，所以您一次性问完或者问多一点，方便您快速地购买到心仪的宝贝。
                    
                    ◆发货时间◆
                    
                    购买时间以买家付款时间为准，正常情况下，每天16点前的订单我们会安排当天发出，如果遇到特殊情况，我们会及时与买家联系，亲们在购买时也可以咨询客服。
                    
                    ◆签收提醒◆
                    
                    买家签收时需本人签收或者委托第三方签收，请买家签收时务必查看外包装是否完整，如有破损，明显挤压变形等，检查所购买商品数量和外观问题，如有问题请立刻联系我们或者拒绝签收，一旦签收了就是默认收到的东西是完好无缺的，如有损失只能由买家自己承担！
                    
                    当面检查签收，请买家朋友收快件的时候，一定要当着派送员的面检查货物，首先检查外包装是否完好，然后打开包裹，检查内件是否和您购买的产品和数量一致，如有任何异常，请不要签字收货，更不要让派送员离开，马上拿起电话，拨打我们运单上面的发件电话，告知实际情况，在经过我们电话确认可以签收的情况下，方可签字收货，让派送员离开，然后尽快上线联系我们售后客服确认，以便尽快解决；如果快递员要求必须先签字，那么签完字后请当着他的面拆包，确认配件完好，如有不对的地方请告知我们来联系快递解决！让派件员离开而没有经过我们确认，货物数量或者外观上面有问题，我们拒绝承担损失~请谅解。
                    
                    对于不能自己亲自签收的客户，我们建议购买的时候通过给我们客服留言的方式，告知我们您什么时间段方便自己签收，我们给您备注在快递单上面，让派送员在指定时间内派送！一定要做到亲自检查签收，所有由于门卫保安家人朋友等代收的快件一律视为本人签收。
                    
                    由于物流的原因，在您签收之前，出现破损或者丢失，我们会在物流确认三天之内给您重新补发
                    
                    ◆退换问题◆
                    
                    所有产品支持七天无理由退换货，购买产品，自签收之时开始（快递官网签收时间为准），七天内，对产品不满意，不喜欢等，在不影响第二次销售的情况下，都可以退换货，你没有确认配件是完好无损、全新原装、一切功能完好之前请不要拆封！请一定记得，如若不然，本店概不退货；
                    
                    由于产品本身存在的问题或者我们的失误造成的退换货，我们承担来回邮费，但需要说明的是，不管客户发回来的邮费是多少，我们给买家承担的返回来的邮费都不超过客户购买时实际收取的邮费金额（例如，买家购买一件产品50元和邮费10元，共计60元，如果由于产品原因，导致退换货，不管买家发回来产生了多少运费，我们最高只承担买家发回来10元邮费，如果购买时折扣优惠了，只算了8元邮费，我们最高也只承担买家发回来8元邮费）
                    
                    由于买家自己的原因不喜欢，买错等等产生的邮费，全部由买家自己承担，发回来以后，请上线联系补差价和邮费，我们收到后第一时间换好发出；
                    
                    所有退换货交易，请买家朋友一定要在包裹里面留一张字条，清晰的写清楚：微信号，姓名，地址，联系电话，订单编号，退换货原因，由于买家发回来的快件，在包裹里面找不到留言字条或者字条模糊看不清楚，我们无法在后台查询到买家交易信息，而造成的换货退款延误，我们不承担责任，请谅解。
                    
                    敬请顾客朋友一定在购买前仔细阅读我们的以上条款。一旦购买本店商品我们就视为接受以上条款，买家事后不能以任何方式拒绝履行以上条款，不能以买前没看见为借口拒绝履行条款。因为您购买商品，仔细阅读购买条款是您应尽的职责，您和我们都必须遵守交易规则。如果您对本店以上观点并不赞同，我们并不建议您购买本店商品！
                    
                    由于商品问题所发回来的快递，由买家先行垫付邮费，到付件全部拒绝签收，等换好或者退货以后，我们按照您购买时支付给我们的邮费金额，打款到支付宝账户或者直接来联系我们申请邮费退款，谢谢您的理解与配合！
                    
                    ◆快递选择◆
                    
                    由于每天订单较多，我们不会对客户的每一个地址去查询是否到达，只要拍下快递，就是默认接受中通申通快递，由于中通或者申通不到造成的时间等损失，本店概不负责！
                    
                    我们同时支持顺丰快递的发送，如需发送顺丰快递，请在订单内备注，感谢您的配合。 """


        if other == "payconfig":
            print("=======================api===================")
            print("接口名称是{0}，接口方法是get".format("payconfig"))
            print("=======================api===================")
            args = request.args.to_dict()
            if "code" not in args or "OMid" not in args:
                return PARAMS_MISS
            print("=======================args===================")
            print(args)
            print("=======================args===================")
            code = args["code"]
            from GroupMeal.config.Inforcode import APP_ID, APP_SECRET_KEY
            request_url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type={3}" \
                .format(APP_ID, APP_SECRET_KEY, code, "authorization_code")
            print("=======================request_url===================")
            print str(request_url)
            print("=======================request_url===================")
            strResult = None
            try:
                import urllib2
                req = urllib2.Request(request_url)
                response = urllib2.urlopen(req)
                strResult = response.read()
                response.close()
                print strResult
            except Exception as e:
                print e.message
            if "openid" not in strResult or "session_key" not in strResult:
                return
            import json
            strResult = json.loads(strResult)
            print("=======================strResult===================")
            print(strResult)
            print("=======================strResult===================")
            openid = strResult["openid"]
            OMid = args["OMid"]
            response = {}
            response["appid"] = APP_ID
            response["openid"] = openid
            import time
            response["timeStamp"] = int(time.time())
            import uuid
            response["nonceStr"] = str(uuid.uuid1()).replace("-", "")
            data = {}
            body = {}
            body["appid"] = APP_ID
            from GroupMeal.config.Inforcode import mch_id
            body["mch_id"] = mch_id
            body["device_info"] = "WEB"
            body["nonce_str"] = str(uuid.uuid1()).replace("-", "")
            body["body"] = "Beauty mirror"
            body["out_trade_no"] = OMid.replace("-", "")
            OMprice = self.sorders.get_omprice_by_omid(OMid)
            print("============OMprice=========")
            print OMprice
            print("============OMprice=========")
            body["total_fee"] = int(OMprice * 100)
            from GroupMeal.config.Inforcode import NETWORK_IP
            body["spbill_create_ip"] = NETWORK_IP
            body["time_start"] = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            body["time_expire"] = (datetime.datetime.now() + datetime.timedelta(hours=2)).strftime("%Y%m%d%H%M%S")
            # TODO 修改响应地址
            body["notify_url"] = "http://123.207.97.185:7444/love/breakfast/other/getdata"
            body["trade_type"] = "JSAPI"
            body["openid"] = openid
            key_sign = "appid={0}&body={1}&device_info={2}&mch_id={3}&nonce_str={4}&notify_url={5}&openid={6}" \
                       "&out_trade_no={7}&time_expire={8}&time_start={9}&total_fee={10}&trade_type={11}".format(
                body["appid"], "Beauty mirror", body["device_info"], body["mch_id"], body["nonce_str"],
                body["notify_url"], body["openid"], body["out_trade_no"], body["time_expire"], body["time_start"],
                body["total_fee"], body["trade_type"]
            )
            from GroupMeal.config.Inforcode import mch_key
            key_sign = key_sign + "&key={0}".format(mch_key)

            import hashlib
            s = hashlib.md5()
            s.update(key_sign)
            body["sign"] = s.hexdigest().upper()
            xml_body = """<xml>\n\t
                            <appid><![CDATA[{0}]]></appid>\n\t
                            <body><![CDATA[{1}]]></body>\n\t
                            <device_info><![CDATA[{2}]]></device_info>\n\t
                            <mch_id><![CDATA[{3}]]></mch_id>\n\t
                            <nonce_str><![CDATA[{4}]]></nonce_str>\n\t
                            <notify_url><![CDATA[{5}]]></notify_url>\n\t
                            <openid><![CDATA[{6}]]></openid>\n\t
                            <out_trade_no><![CDATA[{7}]]></out_trade_no>\n\t
                            <time_expire><![CDATA[{8}]]></time_expire>\n\t
                            <time_start><![CDATA[{9}]]></time_start>\n\t
                            <total_fee><![CDATA[{10}]]></total_fee>\n\t
                            <trade_type><![CDATA[{11}]]></trade_type>\n\t
                            <sign>{12}</sign>\n
                            </xml>\n""".format(body["appid"], "Beauty mirror", body["device_info"], body["mch_id"],
                                               body["nonce_str"],
                                               body["notify_url"], body["openid"], body["out_trade_no"],
                                               body["time_expire"], body["time_start"],
                                               body["total_fee"], body["trade_type"], body["sign"])
            print("=======================body===================")
            print(body)
            print("=======================body===================")
            data["xml"] = body
            strResult = None
            try:
                import urllib2
                url = "https://api.mch.weixin.qq.com/pay/unifiedorder"
                headers = {'Content-Type': 'application/xml'}
                print("=======================xml_body===================")
                print xml_body
                print("=======================xml_body===================")
                req = urllib2.Request(url, headers=headers, data=xml_body)
                url_response = urllib2.urlopen(req)
                strResult = url_response.read()
            except Exception as e:
                print e.message
            print("=======================strResult===================")
            print(str(strResult))
            print("=======================strResult===================")
            if not strResult:
                return
            import xmltodict
            json_strResult = xmltodict.parse(strResult)
            import json
            json_strResult = json.loads(json.dumps(json_strResult))

            json_result = json_strResult["xml"]
            print("=======================json_result===================")
            print(str(json_result))
            print("=======================json_result===================")
            if not json_strResult:
                return
            if "prepay_id" not in json_result:
                return

            prepay_id = json_result["prepay_id"]
            print("=======================prepay_id===================")
            print(str(prepay_id))
            print("=======================prepay_id===================")
            response["package"] = "prepay_id=" + str(prepay_id)
            response["signType"] = "MD5"
            key_sign = "appId={0}&nonceStr={1}&package={2}&signType={3}&timeStamp={4}&key={5}".format(
                response["appid"], response["nonceStr"], response["package"], response["signType"],
                response["timeStamp"], mch_key
            )
            s = hashlib.md5()
            s.update(key_sign)
            response["paySign"] = s.hexdigest().upper()

            return response

        if other == "picture":
            print("=======================api===================")
            print("接口名称是{0}，接口方法是get".format("picture"))
            print("=======================api===================")
            args = request.args.to_dict()
            position = args.get("position")
            print("=======================position===================")
            print("position = ".format(position))
            print("=======================position===================")
            from GroupMeal.config import urlconfig
            htv = "dhdp" if args.get("htv") < 1.6 else "hhdp"
            if position == "top":
                picturelist = [i.format(htv) for i in urlconfig.home]
                print(self.title.format("piclist"))
                print(picturelist)
                print(self.title.format("piclist"))

                return picturelist

            else:
                now = datetime.datetime.now()
                return urlconfig.weekday_pic[now.weekday()].format(htv)

    def post(self, other):
        if other == "getdata":
            print("=======================api===================")
            print("接口名称是{0}，接口方法是get".format("getdata"))
            print("=======================api===================")
            data = request.data
            print "=====================data=================="
            print(data)
            print "=====================data=================="
            import xmltodict
            data = xmltodict.parse(data)
            import json
            data = json.loads(json.dumps(data))

            json_result = data["xml"]
            print(self.title.format("json_result"))
            print(json_result)
            print(self.title.format("json_result"))

            if "return_code" not in json_result:
                print(self.title.format("error"))
                print("not find return_code")
                print(self.title.format("error"))
                return {
                    "return_code": "FAIL",
                    "return_msg": "return_code is not find !!!"
                }

            if json_result.get("return_code") != "SUCCESS":
                print(self.title.format("error"))
                print("return_code is {0}".format(json_result.get("return_code")))
                print(self.title.format("error"))
                return {
                    "return_code": "FAIL",
                    "return_msg": "return_code is not SUCCESS !!!"
                }
            insert_index_list = [8, 13, 18, 23]
            omid_list = list(json_result.get("out_trade_no"))
            for index in insert_index_list:
                omid_list.insert(index, "-")
            omid = "".join(omid_list)
            print(self.title.format("OMid"))
            print(omid)
            print(self.title.format("OMid"))

            try:
                self.sorders.update_order_by_oid(omid, {"OMstatus": 303})
            except Exception as e:
                print(self.title.format("error"))
                print(e.message)
                print(self.title.format("error"))

            return {
                "return_code": "SUCCESS",
                "return_msg": "OK"
            }