"""GARNET logging framework for models

"""

from configobj import ConfigObj
from mantid.kernel import ConfigService


def init_logging():
    """Pass logging configurations from the conf file"""
    conf_svc = ConfigService.Instance()

    LOGGING_CONF = "logging.conf"
    conf = ConfigObj(LOGGING_CONF)

    for option in conf:
        if "logging" in option:
            conf_svc.setString(option, conf[option])
