from flask_restful import Resource
from flask import Flask, request
from lib.apiHandlers.common.ApiConstant import HttpContentType, HttpRequestConstant

from lib.apiHandlers.common.ApiResponse import ApiResponse
from lib.apiHandlers.decorator.AuthenticationDeco import auth_decorator
from lib.apiHandlers.decorator.HttpRequestDeco import httpRequest_decorator
from lib.apiHandlers.exception.InvalidHttpContentTypeException import InvalidHttpContentTypeException
from lib.apiHandlers.exception.InvalidHttpRequestException import InvalidHttpRequestException
from lib.apiHandlers.exception.MissingAttributeException import MissingAttributeException


class HelloRest(Resource):

    #
    @auth_decorator(request=request)
    def get(self) -> tuple[dict[str, any], int]:
        '''
            Get data from url param example
        '''
        try:
            #
            if 'name' not in request.args:
                raise Exception("can't find name")

            name = request.args.get('name')

            #
            response = ApiResponse(status=True, response=name)
            return response.GetApiResponse(), 200

        except Exception as ex:

            response = ApiResponse(
                status=False,
                message=str(ex),
                exception=type(ex).__name__
            )
            return response.GetApiResponse(), 500

    #
    @httpRequest_decorator(request=request, method=HttpRequestConstant.POST, contentType=HttpContentType.JSON, expected=['name', 'lastname'])
    def post(self):
        '''
        get data from post body
        '''
        try:
            #
            request_json = request.get_json()
            print(dict(request_json))

            #
            response = ApiResponse(status=True, response=dict(request_json))
            return response.GetApiResponse(), 200

        except Exception as ex:

            response = ApiResponse(
                status=False,
                message=str(ex),
                exception=type(ex).__name__
            )
            return response.GetApiResponse(), 500

    #
    @httpRequest_decorator(request=request, method=HttpRequestConstant.PUT, contentType=HttpContentType.FORM_URLENCODED, expected=['email', 'password'])
    def put(self):
        '''
        get body from form
        '''
        try:
            #
            email = request.form.get('email')
            password = request.form.get('password')
            print(email, password)

            #
            response = ApiResponse(status=True)
            return response.GetApiResponse(), 200

        except Exception as ex:

            #
            response = ApiResponse(
                status=False,
                message=str(ex),
                exception=type(ex).__name__
            )
            return response.GetApiResponse(), 500
