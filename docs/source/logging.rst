Logging
=========

GARNET uses the Mantid logging framework.

Mantid provides 7 built-in logging levels:
- Debug
- Information
- Notice
- Warning
- Error
- Critical
- Fatal

Mantid convention reserves debug for developers and the rest available to the user.
The information level should be used by default.

Users can configure the logging framework in the GARNET configuration file.

More information is available in the `Mantid logging documentation <https://developer.mantidproject.org/Logging.html>`_.


Logging in Python
-------------------
Developers can access the logger with

.. code-block:: python

		from mantid.kernel import logger
		logger.information("This logs to the information level...")
		logger.error("...and this to the error level.")
