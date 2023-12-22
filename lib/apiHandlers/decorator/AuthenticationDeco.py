from functools import wraps
from flask import Flask, request
import json
import jwt
from lib.apiHandlers.common.ApiResponse import ApiResponse
from lib.apiHandlers.exception.MissingAuthenticationException import MissingAuthenticationException


def auth_decorator(request: request):
    '''
    authentication decorator

    arg: 
        request: flask request object
    '''
    def _auth_decorator(callback):

        #
        @wraps(callback)
        def __auth_decorator(*args, **kwargs):
            try:
                #   1.  get headers
                headers = request.headers

                #   2.  look for authorization token
                auth = headers.get('Authorization')

                #   3.  missing Authorization token
                if auth == None:
                    raise MissingAuthenticationException("Authorization")

                #   decode token
                authTokenArr: list[str] = list(auth.split(' '))

                #   3.  look for custom auth
                customAuth = headers.get('Custom-Auth')

                #   4.  missing Authorization token
                if customAuth is None:
                    raise MissingAuthenticationException("Custom-Auth")

                print('before home')
                result = callback(*args, **kwargs)
                print('after home')

                return result

            except Exception as ex:
                #   create api response object
                response = ApiResponse(
                    status=False,
                    message=str(ex),
                    exception=type(ex).__name__
                )

                #   return to api
                return response.GetApiResponse(), 500

        return __auth_decorator
    return _auth_decorator
