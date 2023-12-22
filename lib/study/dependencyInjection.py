from lib.study.exampleClass import OopExample


class DiExample:
    #
    __oopExample: OopExample

    #
    def __init__(self, oopExample: OopExample) -> None:
        self.__oopExample = oopExample

    #
    def PrinterFromOop(self) -> None:
        self.__oopExample.Print()

    #
    def ExceptionBubbling(self) -> None:
        try:
            raise Exception("A General Exception thrown from bubble example")
        except Exception as e:
            raise e
