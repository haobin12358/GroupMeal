# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from GroupMeal.models.models import Meals
from GroupMeal.services.SBase import SBase, close_session

class SMeals(SBase):

    @close_session
    def get_all_meal_by_msid(self, msid):
        return self.session.query(Meals.MEid, Meals.MEname, Meals.MEimage, Meals.MEprice, Meals.MEtag,
                                  Meals.MEdprice, Meals.MEtype, Meals.MEvolume, Meals.MEfraction, Meals.MEinventory)\
            .filter_by(MSid=msid).filter_by(MEstatus=281).all()

    @close_session
    def get_meal_by_meid(self, meid):
        return self.session.query(Meals.MEname, Meals.MEimage, Meals.MEprice, Meals.MEdprice, Meals.MEtag, Meals.MEinfo,
                                  Meals.MEtype, Meals.MEvolume, Meals.MEfraction, Meals.MEid, Meals.MEinventory,
                                  Meals.MEcalcium, Meals.MEcalorie, Meals.MEcarbohydrate, Meals.MEfat,
                                  Meals.MEinorganic, Meals.MEiron, Meals.MEphosphorus, Meals.MEprotein, Meals.MEweight)\
            .filter_by(MEid=meid).filter_by(MEstatus=281).first()

    @close_session
    def get_meal_nutrition_by_meid(self, meid):
        return self.session.query(Meals.MEid, Meals.MEcalcium, Meals.MEcalorie, Meals.MEcarbohydrate, Meals.MEfat,
                                  Meals.MEinorganic, Meals.MEiron, Meals.MEphosphorus, Meals.MEprotein, Meals.MEweight)\
            .filter_by(MEid=meid).first()

    @close_session
    def update_meal(self, meid, meal):
        self.session.query(Meals).filter_by(MEid=meid).update(meal)
        self.session.commit()
        return True

    @close_session
    def get_all_meal_by_msid_and_metag(self, msid, metag):
        return self.session.query(Meals.MEid, Meals.MEname, Meals.MEimage, Meals.MEprice, Meals.MEtag,
                                  Meals.MEdprice, Meals.MEtype, Meals.MEvolume, Meals.MEfraction, Meals.MEinventory) \
            .filter_by(MSid=msid).filter_by(MEstatus=281).filter_by(MEtag=metag).all()

    @close_session
    def get_all_meal_by_msid_and_metag(self, msid, metype):
        return self.session.query(Meals.MEid, Meals.MEname, Meals.MEimage, Meals.MEprice, Meals.MEtag,
                                  Meals.MEdprice, Meals.MEtype, Meals.MEvolume, Meals.MEfraction, Meals.MEinventory) \
            .filter_by(MSid=msid).filter_by(MEstatus=281).filter_by(MEtype=metype).all()

    @close_session
    def get_all_meal_by_msid_and_metag(self, msid, metag, metype):
        return self.session.query(Meals.MEid, Meals.MEname, Meals.MEimage, Meals.MEprice, Meals.MEtag,
                                  Meals.MEdprice, Meals.MEtype, Meals.MEvolume, Meals.MEfraction, Meals.MEinventory) \
            .filter_by(MSid=msid).filter_by(MEstatus=281).filter_by(MEtag=metag).filter_by(MEtype=metype).all()

    @close_session
    def get_msid_by_meid(self, meid):
        return self.session.query(Meals.MSid).filter_by(MEid=meid).scalar()

    @close_session
    def get_mestatus_by_meid(self, meid):
        return self.session.query(Meals.MEstatus).filter_by(MEid=meid).scalar()