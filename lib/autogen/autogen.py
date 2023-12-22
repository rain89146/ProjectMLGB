from lib.logging.logger import LoggerPy


class AutoGenService:
    #
    logger: LoggerPy
    OpenAiKey: str

    #
    def __init__(self, openAiKey: str, logger: LoggerPy) -> None:
        self.logger = logger
        self.OpenAiKey = openAiKey
        pass
