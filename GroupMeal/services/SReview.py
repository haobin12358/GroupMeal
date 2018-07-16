# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from GroupMeal.models.models import Review
from GroupMeal.services.SBase import SBase, close_session

class SReview(SBase):

    @close_session
    def create_review(self, review):
        self.session.add(review)
        self.session.commit()
        return True

    @close_session
    def get_review(self, oid):
        return  self.session.query(Review.PRid, Review.REscore,
                                             Review.REcontent).filter_by(OMid=oid).all()

    @close_session
    def get_rid_by_uid(self, uid):
        return self.session.query(Review.REid).filter_by(USid=uid).all()
