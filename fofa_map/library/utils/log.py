import logging
import os
import datetime

log_file_name = 'fofa_map.log'

def init_log_file():
    global log_file_name
    if not os.path.exists('logs'):
        os.mkdir('logs')
    log_file_name = 'logs/fofa_map-%s.log' % datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

logging.info('Initializing')
