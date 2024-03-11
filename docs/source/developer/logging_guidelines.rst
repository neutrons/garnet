rst
.. _log-levels-guide:

=============
Logging Guide
=============

Logging is a crucial aspect of software development for tracking and troubleshooting issues.
This guide provides an overview of logging and best practices for using different log levels.

The `garnet.helpers.logger` module provides a simple and consistent interface for logging messages at different levels.
It is a thin wrapper around the `mantid.kernel.Logger <https://developer.mantidproject.org/Logging.html#configuring-the-log-level>`_.

The only difference is that the `garnet.helpers.logger` module provides a mechanism to log Garnet ``debug`` and ``information`` messages
without changing the log level of the Mantid logger. This allows the user to log debug and information messages without the log getting
cluttered with debug and information messages from Mantid. If a user wants to see debug and information messages from Mantid, they can
change the log level in the Mantid preferences. The purpose of this is to facilitate the development and debugging of Garnet without getting
flooded with debug and information messages from Mantid. When the mantid log level is set to information or debug, Mantid will produce an overwhelming
amount of debug and information messages that are not relevant to the development of Garnet.


Log Levels and Best Practices
+++++++++++++++++++++++++++++

Different log levels provide a hierarchy of severity to help developers identify and address problems effectively.
Below are common log levels and guidelines on when to use them:

.. note::

    Logging should only be used in the model. The view and presenter should not contain any logging statements.

Fatal
-----
- **Description:** The most severe log level, indicating a critical error that leads to application termination.
- **When to Use:**
  - Use `fatal` when the application cannot proceed due to a catastrophic failure.
  - Examples include unrecoverable system errors or critical resource unavailability.

Error
-----
- **Description:** Signifies a significant error condition that does not require immediate application termination.
- **When to Use:**
  - Use `error` for unexpected errors that impact the application's functionality but can be handled gracefully.
  - Examples include database connection failures, file not found errors, or invalid user input.

Warning
-------
- **Description:** Indicates potential issues or situations that might lead to errors in the future.
- **When to Use:**
  - Use `warning` for conditions that may cause problems but do not necessarily disrupt the application.
  - Examples include deprecated API usage, low disk space warnings, or non-critical configuration issues.

Notice (Default)
----------------
- **Description:** Provides information about normal, but significant, application events.
- **When to Use:**
  - Use `notice` for noteworthy events that may be of interest but are not considered errors.
  - Examples include successful startup messages, important configuration changes, or periodic system checks.

Information
------------
- **Description:** General information that can be useful for tracking the application's behavior.
- **When to Use:**
  - Use `information` to log routine events, status updates, or informational messages.
  - Examples include user authentication, external API interactions, or state changes within the application.

Debug
-----
- **Description:** Detailed information useful for debugging and troubleshooting during development.
- **When to Use:**
  - Use `debug` for low-level details, variable values, or function call traces.
  - Include `debug` statements during development and testing to identify and resolve issues.


Using the Logger
++++++++++++++++

The `garnet.helpers.logger` module provides a simple mechanism to log messages at different levels.

.. code-block:: python

    from garnet.helpers.logger import Logger

    logger = Logger("FUNCTION_NAME")

    # Log a debug message
    logging.debug('This is a debug message')

    # Log an informational message
    logging.information('This is an informational message')

    # Log a warning message
    logging.warning('This is a warning message')

    # Log an error message
    logging.error('This is an error message')

The log messages will be filtered based on the log level set in the user's Mantid preferences.
The `garnet.helpers.logger` module provides a mechanism to log Garnet ``debug`` and ``information`` messages
without changing the log level of the Mantid logger. To enable this, we would need to run garnet with the following command:

.. code-block:: bash

    garnet --debug

This will enable the Garnet logger to log debug and information messages only within the Garnet codebase.
All mantid log messages will be handled and filtered by the user's Mantid preferences.
