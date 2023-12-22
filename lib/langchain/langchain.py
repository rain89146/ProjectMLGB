from lib.logging.logger import LoggerPy


class LangChainService:
    #
    logger: LoggerPy
    OpenAiKey: str

    #
    def __init__(self, openAiKey: str, logger: LoggerPy) -> None:
        self.logger = logger
        self.OpenAiKey = openAiKey
        pass
