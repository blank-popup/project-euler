# -*- coding: utf-8 -*-
"""Base module for file and logger"""

import logging
import logging.handlers
import sys
import os
import pathlib
from functools import wraps
import time


USE_PYTHON_MODULE = True

k_name_header = 'aha'

def get_filename_from_filepath(Filepath):
    """Get filename from path
    Filepath: filepath
    return: filename"""
    return os.path.basename(Filepath)

def get_logger(Name, Level=logging.DEBUG):
    """Get logger set level. Default level is DEBUG
    Name: name of logger
    Level: level of logger
    return: logger"""
    log = logging.getLogger(Name)
    log.setLevel(Level)
    return log

def set_logger(Logger, Filepath):
    """Set stream and file handler, and excepthook
    Logger: logger
    Filepath: relative filepath of logger
    return: None"""
    format_basic = '[%(asctime)s][%(name)s][%(levelname)s] %(message)s'
    formatter = logging.Formatter(format_basic)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    streamHandler.setLevel(logging.DEBUG)
    Logger.addHandler(streamHandler)
    fileHandler = logging.handlers.RotatingFileHandler(
        os.path.join(dirpath_log, Filepath),
        mode='a',
        maxBytes=104857600, backupCount=100,
        encoding='utf-8'
    )
    fileHandler.setFormatter(formatter)
    fileHandler.setLevel(logging.DEBUG)
    Logger.addHandler(fileHandler)
    sys.excepthook = lambda excType, excValue, traceback: Logger.critical(
        'Exception sys.excepthook', exc_info=(excType, excValue, traceback))

dirpath_log = 'log'
pathlib.Path(dirpath_log).mkdir(parents=True, exist_ok=True)
logger = get_logger(f'{k_name_header}.{__name__}')
dirpath_problems = '../problems'

def tick(Logger=logger):
    """Decoration for logging elapsed time
    Logger: logger"""
    def real_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            time_start = time.perf_counter()
            Logger.info('Start to solve !!!')
            rv = function(*args, **kwargs)
            elapsed = time.perf_counter() - time_start
            Logger.info(f'Elapsed time: [{elapsed}]')
            return rv
        return wrapper
    return real_decorator


def read_file(Filepath):
    """Read file encoded utf-8
    Filepath: filepath for reading
    return: data of file"""
    with open(Filepath, 'r', encoding='utf-8') as f:
        data = f.read()
    return data
