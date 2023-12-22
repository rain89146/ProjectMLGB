class OopExample:
    #   private property
    __debugging: bool = True

    #   stringValue and numberValue
    def __init__(self, StringValue: str, NumberValue: int) -> None:
        self.StringValue = StringValue
        self.NumberValue = NumberValue

    #
    def AssignDebug(self, status: bool) -> None:
        self.__debugging = status

    #
    def GetDebugStatus(self) -> bool:
        return self.__debugging

    #
    def AccessPrivateProperties(self) -> bool:
        '''
        Access the private properties in python
        '''
        return self.__debugging

    #
    def Print(self) -> None:
        print(self.StringValue)

    #
    @staticmethod
    def checkMagician() -> str:
        """
        check if it's magician or not.\n
        Returns:
            string
        """
        isMagician = True
        isExpert = False

        if (isMagician and isExpert):
            return "You are a master magician"
        if (isMagician and not isExpert):
            return "at least you are getting there"
        if (not isMagician):
            return "you need magic power"

    #
    @staticmethod
    def CustomGenerator(num: int):
        """
        custom generator. faster performance, doesn't take memory. returns a generator object.\n
        Args:
            num: The name of the user to greet.
        Returns:
            A generator object
        """
        for i in range(num):
            yield i * 9

    #
    @classmethod
    def CallbackFunctionExample(self, callback) -> None:
        '''
        Callback function example
        Args:
            callback: A callback function when things are done in the mother function
        '''
        # in function property
        myName = "Ryan"

        # execute callback when it's not none
        (callback != None) and callback(myName)
