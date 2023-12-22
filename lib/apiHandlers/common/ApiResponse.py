class ApiResponse:
    status: bool
    message: str
    exception: str
    response: any

    #
    def __init__(self, status: bool, response: any = None, message: str = None, exception: str = None) -> None:
        self.status = status
        self.response = response
        self.message = message
        self.exception = exception

    #   api response
    def GetApiResponse(self) -> dict[str, any]:
        try:
            return {
                'status': self.status,
                'message': self.message,
                'exception': self.exception,
                'response': self.response
            }
        except Exception as ex:
            print(type(ex).__name__)
            raise ex
