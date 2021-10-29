from flask import Flask, request, has_request_context
from config import Config
import os
import logging
from logging.handlers import RotatingFileHandler, SMTPHandler
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)


class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.headers.get('X-Forwarded-For', request.remote_addr)
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)

formatter = RequestFormatter(
    '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
    '[%(asctime)s] %(url)s\n'
    '%(levelname)s in %(module)s: %(message)s\n'
)

# if there is not a logs directory, make one
if not os.path.exists('logs'):
    os.mkdir('logs')
# set up a file handler object
file_handler = RotatingFileHandler('logs/test-log-handle.log', maxBytes=10240, backupCount=10)
#  write to file under these circumstances
# low to high: NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
app.logger.addHandler(file_handler)

app.logger.setLevel(logging.INFO)
app.logger.info('App startup')

# # EMAIL SETUP FOR LOGGING
# if not app.debug:
#     if app.config['MAIL_SERVER']:
#         auth = None
#         if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
#             auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
#         secure = None
#         if app.config['MAIL_USE_TLS']:
#             secure = ()
#         mail_handler = SMTPHandler(
#             mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
#             fromaddr='no-reply@' + app.config['MAIL_SERVER'],
#             toaddrs=app.config['ADMINS'], subject='Portfolio Failure',
#             credentials=auth, secure=secure)
#         mail_handler.setLevel(logging.INFO)
#         app.logger.addHandler(mail_handler)

# instance of Mail() for contacting Blake
mail = Mail(app)


from app import routes, errors