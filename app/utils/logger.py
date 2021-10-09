"""
    @title: Logger
    @description: Custom logger for python project
    @uses: using log object call logs method.
"""
# standard modules import
import logging

# defining log format
from colorlog import ColoredFormatter


def logger():
    log = logging.getLogger(__name__)
    ch = logging.StreamHandler()
    formatter = ColoredFormatter(
        '%(log_color)s %(levelname)-8s [%(filename)s:%(lineno)d - %(funcName)10s()] %(message)s ',
        '%c')
    ch.setFormatter(formatter)
    log.addHandler(ch)
    log.setLevel(logging.DEBUG)
    log.propagate = False
    return log
