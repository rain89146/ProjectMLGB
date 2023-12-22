
from functools import reduce
from lib.study.exampleClass import OopExample
from lib.study.dependencyInjection import DiExample
from lib.study.customException import SalaryNotRangeException
from lib.study.dataTypeExample import DataStructure
from lib.study.LambdaAndFunctions import LambdaAndFunctionExample

try:
    oop = OopExample("hello", 18)

    # assign private attribute
    oop.AssignDebug(False)
    status = oop.GetDebugStatus()
    print(status)

    #
    lambdaFun = LambdaAndFunctionExample()

    diExp = DiExample(oop)
    diExp.PrinterFromOop()

    #
    ds = DataStructure()
    ds.ListComprehensionExample()
    ds.SetComprehensionExample()
    ds.DictionaryComprehensionExample()

    # # exception bubbling
    # diExp.ExceptionBubbling();

    # # throw exception
    # raise SalaryNotRangeException(900);

    # ds = DataStructure();
    # ds.PrintTheDic();

    # ds.FillingDic();

    #
    # ds.AcceptParam({'a': "12344", 'b': "2abc12", 'c': "what the fuck?", 'd': "55"})

    myDic: dict[str, str] = {'a': "12344", 'b': "2abc12"}

    # if (myDic.get('a')):
    #     print(type(myDic['a']).__name__);

    # # try to get d, if d not exists set default value for d
    # d: str = myDic.get('d', "DefaultDValue")
    # print(d);

    # c = myDic.get('c');
    # if (c == None) : raise Exception("Fucking none")
    # print(c)

    # immutable list, can not be changed. can not sort. only read, faster than array
    myTuple: tuple[int, ...] = (1, 2, 3, 4, 5)

    # an unique array
    mySet: set[int] = {1, 2, 3, 4, 5}
    myNewSet: set[int] = mySet.copy()
    mySetList: list[int] = list(mySet)
    isExist: bool = 1 in mySet

    # in js or other language isTrue = (0 < 9) ? True : False
    isTrue: bool = True if 0 < 8 else False

    #
    res = oop.checkMagician()
    print(res)

    # custom generator
    listOfTen = oop.CustomGenerator(10)
    # for item in listOfTen:
    #     print(item)

    # lambda way
    oop.CallbackFunctionExample(lambda myName: print(myName))

    # callback way
    def myCallback(myName: str) -> None: print(myName)
    oop.CallbackFunctionExample(myCallback)

    # closure

    def ExampleClosure() -> dict[str, callable]:
        c: int = 20

        #
        def closureFunction() -> int:
            a: int = 1
            b: int = 2
            return a + b + c
        #

        def cleaning(name: str) -> None:
            print("{} cleaned".format(name))

        #
        return {
            'closureFunction': closureFunction,
            'cleaning': cleaning
        }

    # res = ExampleClosure()['cleaning']("ryan");
    # print(res)

    #

    def ExampleDecorator(fn):
        #
        def wrapper(*args, **kwargs):
            print("running")
            res = fn(*args, **kwargs)
            print("done")
            return res
        #
        return wrapper

    @ExampleDecorator
    def TestOutDeco() -> list[int]:
        arr: list[int] = []
        for i in range(100):
            arr.append(i*5)
        return arr

    # arr: list[int] = TestOutDeco();
    # print(arr);

    def fib(number: int) -> list[int]:
        a = 0
        b = 1
        for i in range(number):
            yield a
            temp = a
            a = b
            b = temp + b

    # for i in fib(21): print(i)

    SampleArray = [1, 2, 3]
    tuples = [(0, 2), (4, 3), (9, 9), (0, -1)]

    multiplyArray: list[int] = lambdaFun.ItemMultiplier(SampleArray)
    print(multiplyArray)

    oddOnly = lambdaFun.ItemFilterOddOnly(SampleArray)
    print(oddOnly)

    zipExample: list[tuple[int, int, int]] = lambdaFun.ZipperFunction()
    print(zipExample)

    #   reduce an array to a value
    reduceExample: int = lambdaFun.ItemReducer(SampleArray)
    print(reduceExample)

    # sort array of int
    squareArr: list[int] = lambdaFun.SquareLambda(SampleArray)
    print(squareArr)

    # sort array of tuple
    sortedTuple: list[tuple[int]] = lambdaFun.SortTuple(tuples)
    print(sortedTuple)


except SalaryNotRangeException as SalaryException:
    print(type(SalaryException).__name__)
    print(str(SalaryException))

except Exception as e:
    print(type(e).__name__)
    print(str(e))
