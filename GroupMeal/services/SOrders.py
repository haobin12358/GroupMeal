# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from GroupMeal.models.models import OrderMain, OrderPart
from GroupMeal.services.SBase import SBase, close_session


class SOrders(SBase):

    @close_session
    def update_order_by_oid(self, oid, order):
        self.session.query(OrderMain).filter_by(OMid=oid).update(order)
        return True

    @close_session
    def get_all_order_by_uid(self, uid):
        return self.session.query(OrderMain.OMid, OrderMain.OMtime, OrderMain.OMstatus,
                                  OrderMain.OMtotal, OrderMain.OMcode).filter_by(
            USid=uid).order_by(OrderMain.OMtime.desc()).all()

    @close_session
    def get_order_item_by_oid(self, oid):
        return self.session.query(OrderPart.MEnumber, OrderPart.MEid).filter_by(OMid=oid).all()

    @close_session
    def get_order_abo_by_oid(self, oid):
        return self.session.query(OrderMain.OMid, OrderMain.OMtime, OrderMain.OMtotal, OrderMain.CPid,
                                  OrderMain.OMcode, OrderMain.OMabo, OrderMain.OMstatus) \
            .filter_by(OMid=oid).first()

    @close_session
    def get_omstatus_by_omid(self, omid):
        return self.session.query(OrderMain.OMstatus).filter_by(OMid=omid).scalar()

    @close_session
    def get_omprice_by_omid(self, omid):
        return self.session.query(OrderMain.OMtotal).filter_by(OMid=omid).scalar()

    @close_session
    def get_order_main_by_code(self, omcode):
        return self.session.query(OrderMain.OMid, OrderMain.OMcode)\
            .filter(OrderMain.OMcode == omcode, OrderMain.OMstatus < 42).first()

    @close_session
    def get_usid_by_omid(self, omid):
        return self.session.query(OrderMain.USid).filter_by(OMid=omid).scalar()

    @close_session
    def get_all_order_by_time(self, timestart, timeend, usid):
        return self.session.query(OrderMain.OMid)\
            .filter(OrderMain.OMtime >= timestart, OrderMain.USid == usid, OrderMain.OMtime <= timeend,
                    OrderMain.OMstatus >= 305, OrderMain.OMstatus <= 306)\
            .all()