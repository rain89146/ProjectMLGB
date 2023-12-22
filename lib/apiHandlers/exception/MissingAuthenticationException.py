class MissingAuthenticationException(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, MissingAuthenticationName: str, message: str = "Missing authentication attribute, '{}' was missing"):
        self.message = message.format(MissingAuthenticationName)
        super().__init__(self.message)
