# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from GroupMeal.models.models import Mess
from GroupMeal.services.SBase import SBase, close_session
from GroupMeal.common.TransformToList import trans_params

class SMess(SBase):

    @close_session
    def get_mess_by_city(self, mscity):
        return self.session.query(Mess.MSid, Mess.MSname).filter_by(MScity=mscity).filter_by(MSstatus=501).all()

    @close_session
    def get_mess_by_msid(self, msid):
        return self.session.query(Mess.MSid, Mess.MSname, Mess.MSimage, Mess.MSlocation, Mess.MStelphone,
                                  Mess.MStimestart, Mess.MStimeend, Mess.MStrueimage, Mess.MShealthimage,
                                  Mess.MShealthlevel).filter_by(MSid=msid).first()

    @close_session
    def update_mess(self, msid, mess):
        self.session.query(Mess).filter_by(MSid=msid).update(mess)
        return True

    @trans_params
    @close_session
    def get_all_city(self):
        return self.session.query(Mess.MScity).all()