# *- coding:utf8 *-
import datetime
import base64

def usid_to_token(usid):
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    token_without_base = usid + "#" + time_now
    token_with_base = base64.b64encode(token_without_base)
    return token_with_base

def token_to_usid(token):
    token_without_base = base64.b64decode(token)
    usid_time = token_without_base.split("#")
    return usid_time[0]