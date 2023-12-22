import logging
import sys
from pythonjsonlogger import jsonlogger


class LoggerPy:

    #   logger instance
    logger: logging.Logger

    #   initiate logger
    def __init__(self) -> None:

        # create logger instance
        logger: logging.Logger = logging.getLogger(__name__)

        # standard output handler
        stdoutHandler = logging.StreamHandler(stream=sys.stdout)

        # set the log levels on the handlers
        stdoutHandler.setLevel(logging.INFO)

        # create format
        format = jsonlogger.JsonFormatter(
            "%(name)s %(asctime)s %(levelname)s %(filename)s %(lineno)s %(process)d %(message)s %(stack_info)s",
            rename_fields={
                "levelname": "severity",
                "asctime": "timestamp",
                "stack_info": "stack"
            },
            json_indent=4
        )

        # set format
        stdoutHandler.setFormatter(format)

        # add handlers to logger
        logger.addHandler(stdoutHandler)

        # assign logger
        self.logger = logger

    #   information log
    def InfoLog(self, message: any) -> None:
        self.logger.info(message, stack_info=False)

    #   debug log
    def DebugLog(self, message: any) -> None:
        self.logger.debug(message, stack_info=True, exc_info=True)

    #   error log
    def ErrorLog(self, message: any) -> None:
        self.logger.error(message, stack_info=True, exc_info=True)

    #   warning log
    def WarningLog(self, message: any) -> None:
        self.logger.warning(message, stack_info=True)

    #   critical log
    def CriticalLog(self, message: any) -> None:
        self.logger.critical(message, stack_info=True)
