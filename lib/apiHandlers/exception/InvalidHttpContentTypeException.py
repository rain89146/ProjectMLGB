class InvalidHttpContentTypeException(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, ExpectedContentType: str, IncomingContentType: str, message: str = 'Invalid http request content type received, {} was expected, but {} was received'):
        self.message = message.format(
            ExpectedContentType,
            IncomingContentType
        )
        super().__init__(self.message)
