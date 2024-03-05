"""

GARNET logging framework for models

"""

from mantid.kernel import logger
from mantid.kernel import ConfigService


from configobj import ConfigObj



def init_logging():
    """
    Pass logging configurations from the conf file
    """

    conf_svc = ConfigService.Instance()

    LOGGING_CONF = "logging.conf"
    conf = ConfigObj(LOGGING_CONF)
    
    for option in conf:
        if 'logging' in option:    
            conf_svc.setString(option, conf[option])


    











