# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
import DBSession
from GroupMeal.common.lovebreakfast_error import dberror
import GroupMeal.models.models as models


def close_session(fn):
    def inner(self, *args, **kwargs):
        try:
            result = fn(self, *args, **kwargs)
            self.session.commit()
            return result
        except Exception as e:
            print("DBERROR" + e.message)
            self.session.rollback()
            raise dberror(e.message)
        finally:
            self.session.close()
    return inner


# service 基础类
class SBase(object):
    def __init__(self):
        try:
            self.session = DBSession.db_session()
        except Exception as e:
            print(e.message)

    @close_session
    def add_model(self, model_name, **kwargs):
        print(model_name)
        if not getattr(models, model_name):
            print("model name = {0} error ".format(model_name))
            return
        model_bean = eval(" models.{0}()".format(model_name))
        for key in model_bean.__table__.columns.keys():
            if key in kwargs:
                setattr(model_bean, key, kwargs.get(key))

        self.session.add(model_bean)
