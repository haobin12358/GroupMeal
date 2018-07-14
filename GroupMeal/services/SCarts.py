# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from GroupMeal.models.models import Cart
from GroupMeal.services.SBase import SBase, close_session


class SCarts(SBase):

    def __init__(self):
        super(SCarts, self).__init__()

    @close_session
    def get_carts_by_Uid(self, uid):
        return self.session.query(Cart.CAid, Cart.MEid, Cart.CAnumber).filter_by(USid=uid).all()

    # @close_session
    # def add_carts(self, **kwargs):
    #     cart = Cart()
    #     for key in cart.__table__.columns.keys():
    #         if key in kwargs:
    #             setattr(cart, key, kwargs.get(key))
    #     self.session.add(cart)

    @close_session
    def del_carts(self, caid):
        self.session.query(Cart).filter_by(CAid=caid).delete()

    @close_session
    def update_num_cart(self, pnum, caid):
        self.session.query(Cart).filter_by(CAid=caid).update({"CAnumber": pnum})

    @close_session
    def get_cart_by_usid_meid(self, usid, meid):
        return self.session.query(Cart.CAid, Cart.CAnumber).filter_by(USid=usid).filter_by(MEid=meid).first()

    @close_session
    def get_canumber_by_meid_and_usid(self, meid, usid):
        return self.session.query(Cart.CAnumber).filter_by(MEid=meid).filter_by(USid=usid).scalar()

    @close_session
    def get_prid_by_caid(self, caid):
        return self.session.query(Cart.MEid).filter(Cart.CAid == caid).scalar()