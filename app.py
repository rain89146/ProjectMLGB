
from lib.apiHandlers.example.HelloRest import HelloRest
from lib.autogen.autogen import AutoGenService
from lib.langchain.langchain import LangChainService
from lib.logging.logger import LoggerPy
from flask import Flask
from flask_restful import Resource, Api
from flask_socketio import SocketIO
from dotenv import load_dotenv
import os

try:
    # load env file
    load_dotenv()

    # load open ai key
    OPENAI_KEY = os.getenv('OPENAI_KEY')

    # create flask server
    app = Flask(__name__)
    api = Api(app)
    socketio = SocketIO(app)

    # create logger
    logger = LoggerPy()

    # load autogen service
    autoGen = AutoGenService(openAiKey=OPENAI_KEY, logger=logger)
    langChain = LangChainService(openAiKey=OPENAI_KEY, logger=logger)

    apiVersion = 'v1'
    apiPath = f'/api/{apiVersion}/'

    helloRest = HelloRest()

    # Hello rest example
    api.add_resource(HelloRest, f'{apiPath}/HelloRest/')

    #
    if __name__ == '__main__':
        app.run(debug=True, port=1994, host="localhost")

except Exception as e:
    logger.ErrorLog(e)
