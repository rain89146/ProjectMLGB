class InvalidHttpRequestException(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, ExpectedRequestMethod: str, IncomingRequestMethod: str, message: str = 'Invalid http request method received, {} was expected, but {} was received'):
        self.message = message.format(
            ExpectedRequestMethod,
            IncomingRequestMethod
        )
        super().__init__(self.message)
