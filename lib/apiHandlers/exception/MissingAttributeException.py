class MissingAttributeException(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, MissingAttributeName: str, message: str = "Missing attribute in payload, '{}' was missing"):
        self.message = message.format(MissingAttributeName)
        super().__init__(self.message)
