# *- coding:utf8 *-
from flask import Flask
import flask_restful

gm = Flask(__name__)
api = flask_restful.Api(gm)

'''
if __name__ == '__main__':
    gm.run('0.0.0.0', 443, debug=True, ssl_context=(
        "/etc/nginx/cert/1525609592348.pem"
    ))
'''
if __name__ == '__main__':
    gm.run('0.0.0.0', 7444, debug=True)
