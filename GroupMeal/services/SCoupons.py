# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from GroupMeal.models.models import Cardpackage
from GroupMeal.services.SBase import SBase, close_session
from GroupMeal.models.models import Coupons


class SCoupons(SBase):
    def __init__(self):
        super(SCoupons, self).__init__()

    @close_session
    def get_cardpackage_by_uid(self, uid):

        return self.session.query(
            Cardpackage.COid, Cardpackage.CPid,
            Cardpackage.USid
        ).filter(Cardpackage.USid == uid).all()

    @close_session
    def add_coupons(self, **kwargs):
        coupons = Coupons()
        for key in coupons.__table__.columns.keys():
            if key in kwargs:
                setattr(coupons, key, kwargs.get(key))
        self.session.add(coupons)

    @close_session
    def add_cardpackage(self, **kwargs):
        cardpackage = Cardpackage()
        for key in cardpackage.__table__.columns.keys():
            if key in kwargs:
                setattr(cardpackage, key, kwargs.get(key))
        self.session.add(cardpackage)

    @close_session
    def update_carbackage(self, cardid):
        self.session.query(Cardpackage).filter(Cardpackage.CPid == cardid).update({"CAstatus": 2})

    @close_session
    def get_card_by_uid_couid(self, uid, couid):
        return self.session.query(
            Cardpackage.COid, Cardpackage.CPid, Cardpackage.USid
        ).filter(Cardpackage.USid == uid, Cardpackage.COid == couid).first()

    @close_session
    def get_coupons_by_couid(self, couid):
        return self.session.query(
            Coupons.COid, Coupons.COamount, Coupons.COdiscount,
            Coupons.COstart, Coupons.COend, Coupons.COfilter, Coupons.COtype
        ).filter(Coupons.COid == couid).first()
