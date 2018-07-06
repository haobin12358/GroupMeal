# *- coding:utf8 *-
# 兼容linux系统
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))  # 增加系统路径
sys.path.append(os.path.dirname(os.getcwd()))  # 增加系统路径
import models.model as models


# 装饰器，用来解析数据库获取的内容，将获取到的对象转置为dict，将获取到的单个数据的tuple里的数据解析出来
def trans_params(func):
    def inner(*args, **kwargs):
        params = func(*args, **kwargs)
        result = []
        if params:
            for param in params:
                if isinstance(param, (list, tuple)):
                    data = param[0]
                    # 如果发现解析的数据是Unicode 转置为utf-8
                    if isinstance(data, unicode):
                        data = data.encode("utf8")
                    result.append(data)
                elif isinstance(param, models.Base):
                    param_dict = param.__dict__
                    for param_key in param_dict:
                        # 所有的model的dict里都有这个不需要的参数，所以删除掉
                        if param_key == "_sa_instance_state":
                            continue
                        # 如果发现解析到的数据是Unicode 转置为utf-8
                        if isinstance(param_dict.get(param_key), unicode):
                            param_dict[param_key] = param_dict.get(param_key).encode("utf8")

                    result.append(param_dict)
                else:
                    result = params
        return result

    return inner


def add_model(model_name, **kwargs):
    print(model_name)
    if not getattr(models, model_name):
        print("model name = {0} error ".format(model_name))
        return
    model_bean = eval(" models.{0}()".format(model_name))
    for key in model_bean.__table__.columns.keys():
        if key in kwargs:
            setattr(model_bean, key, kwargs.get(key))
    from services.DBSession import get_session
    session, status = get_session()
    if status:
        session.add(model_bean)
        session.commit()
        session.close()
        return
    raise Exception("session connect error")
