# *- coding:utf-8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine, Integer, String, Text, Float
from GroupMeal.config import dbconfig as cfg

DB_PARAMS = "{0}://{1}:{2}@{3}/{4}?charset={5}".format(
    cfg.sqlenginename, cfg.username, cfg.password, cfg.host, cfg.database, cfg.charset)
mysql_engine = create_engine(DB_PARAMS, echo=False)
Base = declarative_base()

class Users(Base):
    __tablename__ = "Users"
    USid = Column(String(64), primary_key=True)         # 主键
    USname = Column(String(64), nullable=False)         # 昵称
    UStelphone = Column(String(14), nullable=False)     # 联系方式
    USpassword = Column(String(16), nullable=False)     # 密码
    USlevel = Column(Integer, nullable=False, default=0)# 等级{0-7，默认0}
    USemail = Column(Text)                              # 邮箱  # 邮箱验证待定
    UScoin = Column(Float, nullable=False, default=0)   # 积分
    USinvatecode = Column(String(7), nullable=False)    # 邀请码
    USavatar = Column(Text)                             # 头像  # 头像修改方式待定
    USsex = Column(Integer)                             # 性别{101男，102女}
    USheight = Column(Float)                            # 身高
    USweight = Column(Float)                            # 体重
    USbirthday = Column(String(8))                      # 生日
    USworker = Column(Text)                             # 职业
    UScardno = Column(String(18))                       # 身份证号
    USmedicalhistory = Column(Text)                     # 疾病史
    USsightleft = Column(Float)                         # 视力（左）
    USsightright = Column(Float)                        # 视力（右）
    USbpressurehigh = Column(Integer)                   # 血压（高）
    USbpressurelow = Column(Integer)                    # 血压（低）

class Meals(Base):
    __tablename__ = "Meals"
    MEid = Column(String(64), primary_key=True)         # 主键
    MEname = Column(String(128), nullable=False)        # 餐品名称
    MEimage = Column(Text, nullable=False)              # 餐品图片
    MEinfo = Column(Text)                               # 餐品详情
    MEprice = Column(Float, nullable=False)             # 餐品价格
    MEdprice = Column(Float)                            # 餐品折扣价
    MEvolume = Column(Integer, nullable=False, default=0)# 餐品销量
    MEfraction = Column(Float, nullable=False, default=0)# 餐品评分
    MSid = Column(String(64), nullable=False)           # 食堂id
    MEweight = Column(Float)                            # 餐品分量
    MEtype = Column(Integer, nullable=False)            # 餐品分类
    # {200肉类201特色餐饮202套餐203素食204汤菜205面食206粥点207早餐}
    MEtag = Column(Integer, nullable=False)             # 餐品标签
    # {291热销292活动商品293推广商品294广告商品295网红商品296新品}
    MEstatus = Column(Integer, nullable=False)          # 餐品状态
    # {281在售，282下架， 283待审核}
    MEinventory = Column(Integer)                       # 库存
    MEprotein = Column(Float)                           # 蛋白质
    MEfat = Column(Float)                               # 脂肪
    MEcarbohydrate = Column(Float)                      # 碳水化合物
    MEcalorie = Column(Float)                           # 卡路里
    MEinorganic = Column(Float)                         # 无机盐
    MEcalcium = Column(Float)                           # 钙
    MEphosphorus = Column(Float)                        # 磷
    MEiron = Column(Float)                              # 铁

class Mess(Base):
    __tablename__ = "Mess"
    MSid = Column(String(64), primary_key=True)         # 主键
    MSname = Column(String(128), nullable=False)        # 食堂名称
    MSlocation = Column(Text, nullable=False)           # 食堂地点
    MSimage = Column(Text, nullable=False)              # 食堂图
    MStelphone = Column(String(14), nullable=False)     # 联系方式
    MStimestart = Column(String(6))                     # 预约起始时间
    MStimeend = Column(String(6))                       # 预约结束时间
    MStrueimage = Column(Text)                          # 营业许可证
    MShealthimage = Column(Text)                        # 健康许可证
    MShealthlevel = Column(String(1))                   # 卫生指标
    MScity = Column(String(128), nullable=False)        # 所在城市

class OrderMain(Base):
    __tablename__ = "OrderMain"
    OMid = Column(String(64), primary_key=True)         # 主键
    OMtime = Column(String(14), nullable=False)         # 下单时间
    USid = Column(String(64), nullable=False)           # 用户id
    OMtotal = Column(Float, nullable=False)             # 订单总价
    OMstatus = Column(Integer, nullable=False)          # 订单状态
    # {301未支付302支付中303已支付304待取餐305已取餐306已评价307退款中308已退款309已取消310申请退款}
    OMcode = Column(String(6), nullable=False)          # 取餐码
    OMabo = Column(Text)                                # 订单备注
    CPid = Column(String(64), nullable=False)           # 卡包内优惠券id

class OrderPart(Base):
    __tablename__ = "OrderPart"
    OPid = Column(String(64), primary_key=True)         # 主键
    OMid = Column(String(64), nullable=False)           # 订单id
    MEid = Column(String(64), nullable=False)           # 餐品id
    MEnumber = Column(Integer, nullable=False)          # 餐品数量

class Cart(Base):
    __tablename__ = "Cart"
    CAid = Column(String(64), primary_key=True)         # 主键
    USid = Column(String(64), nullable=False)           # 用户id
    MEid = Column(String(64), nullable=False)           # 餐品id
    CAnumber = Column(Integer)                          # 商品在购物车中的数量

class Review(Base):
    __tablename__ = "Review"
    REid = Column(String(64), primary_key=True)         # 主键
    OMid = Column(String(64), nullable=False)           # 订单id
    MEid = Column(String(64), nullable=False)           # 餐品id
    REscore = Column(Float, nullable=False)             # 餐品评分
    REcontent = Column(Text)                            # 评价内容

class Coupons(Base):
    __tablename__ = "Coupon"
    COid = Column(String(64), primary_key=True)         # 主键
    COfilter = Column(Float)                            # 优惠券优惠条件，到达金额
    COdiscount = Column(Float)                          # 折扣，值为0-1，其中0为免单
    COamount = Column(Float)                            # 优惠金额，减免金额，限制最大数目
    COstart = Column(String(14))                        # 优惠券的开始时间
    COend = Column(String(14))                          # 优惠券的结束时间
    COtype = Column(Integer)                            # 优惠券的类型 {801 满减， 802 满折， 803 商品类目限制， 804 无限制， 805 用户类型限制}

class Cardpackage(Base):
    __tablename__ = "Cardpackage"
    CPid = Column(String(64), primary_key=True)         # 主键
    USid = Column(String(64), nullable=False)           # 用户id
    COid = Column(String(64), nullable=False)           # 优惠券id


class IdentifyingCode(Base):
    __tablename__ = "IdentifyingCode"
    ICid = Column(String(64), primary_key=True)         # 主键
    ICtelphone = Column(String(14), nullable=False)     # 获取验证码的手机号
    ICcode = Column(String(8), nullable=False)          # 获取到的验证码
    ICtime = Column(String(14), nullable=False)         # 获取的时间


class BlackUsers(Base):
    __tablename__ = "BlackUsers"
    BUid = Column(String(64), primary_key=True)         # 主键
    BUtelphone = Column(String(14), nullable=False)     # 黑名单电话
    BUreason = Column(Text)                             # 加入黑名单的原因

if __name__ == "__main__":
    '''
    运行该文件就可以在对应的数据库里生成本文件声明的所有table
    '''
    Base.metadata.create_all(mysql_engine)