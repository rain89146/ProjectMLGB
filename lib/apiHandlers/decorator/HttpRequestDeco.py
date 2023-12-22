from functools import wraps
from flask import Flask, request

from lib.apiHandlers.common.ApiConstant import HttpContentType
from lib.apiHandlers.common.ApiResponse import ApiResponse
from lib.apiHandlers.exception.InvalidHttpContentTypeException import InvalidHttpContentTypeException
from lib.apiHandlers.exception.InvalidHttpRequestException import InvalidHttpRequestException
from lib.apiHandlers.exception.MissingAttributeException import MissingAttributeException


def httpRequest_decorator(request: request, method: str, contentType: str, expected: list[str]):
    '''
    Http decorator

    arg: 
        request: flask request object
        method: expected request method
        contentType: accept content type
        expected: expected attribute
    '''
    def _httpRequest_decorator(callback):

        #
        @wraps(callback)
        def __httpRequest_decorator(*args, **kwargs):
            try:
                #   1. invalid request type
                if request.method != method:
                    raise InvalidHttpRequestException(method, request.method)

                #   2. invalid content type
                if request.mimetype is None or request.mimetype != contentType:
                    raise InvalidHttpContentTypeException(
                        contentType,
                        request.mimetype if request.mimetype is None else "empty"
                    )

                #   3.a when the content type is application/x-www-form-urlencoded
                if request.mimetype == HttpContentType.FORM_URLENCODED:
                    for item in expected:
                        if item not in list(request.form.to_dict().keys()):
                            raise MissingAttributeException(item)

                #   3.b. when the content type is application/json
                if request.mimetype == HttpContentType.JSON:

                    #   when the json is empty
                    if not request.get_json():
                        raise MissingAttributeException("Empty")

                    #
                    for item in expected:
                        if item not in list(dict(request.get_json()).keys()):
                            raise MissingAttributeException(item)

                #   4. keep going
                return callback(*args, **kwargs)

            except Exception as ex:
                #   create api response object
                response = ApiResponse(
                    status=False,
                    message=str(ex),
                    exception=type(ex).__name__
                )

                #   return to api
                return response.GetApiResponse(), 500

        return __httpRequest_decorator
    return _httpRequest_decorator
