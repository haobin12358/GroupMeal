# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
import uuid
from GroupMeal.models.models import Users, IdentifyingCode
from GroupMeal.common.TransformToList import trans_params
from GroupMeal.services.SBase import SBase, close_session

class SUsers(SBase):
    @trans_params
    @close_session
    def get_all_user_tel(self):
        return self.session.query(Users.UStelphone).all()

    @close_session
    def login_users(self, utel, upwd, usinvatecode):
        new_user = Users()
        new_user.USid = str(uuid.uuid1())
        new_user.UStelphone = utel
        new_user.USpassword = upwd
        new_user.USname = "昵称" + utel
        new_user.USsex = None
        new_user.UScoin = 0
        new_user.USinvatecode = usinvatecode
        new_user.USlevel = 0
        new_user.USemail = None
        new_user.USavatar = "图片地址"
        self.session.add(new_user)
        return True

    @close_session
    def get_upwd_by_utel(self, utel):
        return self.session.query(Users.USpassword).filter_by(UStelphone=utel).scalar()

    @close_session
    def update_users_by_uid(self, uid, users):
        self.session.query(Users).filter_by(USid=uid).update(users)
        self.session.commit()
        self.session.close()
        return True

    @close_session
    def get_all_users_info(self, usid):
        return self.session.query(Users.USname, Users.UStelphone, Users.USsex, Users.UScoin,
                                  Users.USinvatecode, Users.USavatar, Users.USemail, Users.USlevel) \
            .filter_by(USid=usid).first()

    @close_session
    def get_first_user_info(self, usid):
        return self.session.query(Users.USbirthday, Users.USheight, Users.USweight, Users.USworker, Users.UScardno)\
            .filter_by(USid=usid).first()

    @close_session
    def get_uname_utel_by_uid(self, uid):
        return self.session.query(Users.USname, Users.UStelphone).filter_by(USid=uid).first()

    @close_session
    def get_uptime_by_utel(self, utel):
        return self.session.query(IdentifyingCode.ICtime).filter_by(ICtelphone=utel) \
            .order_by(IdentifyingCode.ICtime.desc()).first()

    @close_session
    def get_code_by_utel(self, utel):
        return self.session.query(IdentifyingCode.ICcode).filter_by(ICtelphone=utel) \
            .order_by(IdentifyingCode.ICtime.desc()).first()

    @close_session
    def add_inforcode(self, utel, code, time):
        new_infocode = IdentifyingCode()
        new_infocode.ICid = str(uuid.uuid1())
        new_infocode.ICtelphone = utel
        new_infocode.ICcode = code
        new_infocode.ICtime = time
        self.session.add(new_infocode)
        return True

    @close_session
    def get_user_by_utel(self, utel):
        return self.session.query(Users.USid).filter_by(UStelphone=utel).first()

    @trans_params
    @close_session
    def get_all_invate_code(self):
        return self.session.query(Users.USinvatecode).all()

    @close_session
    def get_user_by_usid(self, usid):
        return self.session.query(Users.USid, Users.UStelphone, Users.USinvatecode) \
            .filter_by(USid=usid).all()

    @close_session
    def get_uid_by_utel(self, utel):
        return self.session.query(Users.USid).filter_by(UStelphone=utel).scalar()

    @close_session
    def get_uslevel_by_usid(self, uid):
        return self.session.query(Users.USlevel).filter_by(USid=uid).scalar()

    @close_session
    def get_first_user_by_usid(self, usid):
        return self.session.query(Users.USweight, Users.USheight, Users.USbirthday, Users.UScardno, Users.USworker)\
            .filter_by(USid=usid).first()

