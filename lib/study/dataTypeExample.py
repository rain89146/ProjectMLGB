from typing import TypeVar, Generic, Sequence, Union, Any, Optional, Callable
from collections.abc import Sized, Iterable, Iterator


class DataStructure:
    StringDicType = dict[str, str]

    # set
    CustomIntSet: set[int] = {1, 2, 3, 4, 5}

    # dictionary 1
    CustomStringDic: dict[str, str] = {'a': "12344", 'b': "2abc12"}
    CustomIntDic: dict[str, int] = {'a': 4, 'b': 5}

    # tuple
    CustomIntTuple: tuple[int, ...] = (1, 2, 3, 4, 5)
    CustomStrTuple: tuple[str, ...] = ("a", "b", "c")

    # list (array)
    CustomIntList: list[int] = [1, 2, 3, 4]

    # matrix
    CustomMatrix = list[list[int]] = [
        [1, 2, 3],
        [3, 5, 6],
        [7, 8, 9]
    ]

    #   empty dic
    EmptyIntDic: dict[str, int] = {}

    def __init__(self) -> None:
        self.ExampleDic = {'a': 1, 'b': "2", 'c': 0}
        self.EmptyDic = dict()

    def ListFunctions(self) -> None:
        # copy a list
        newList = self.CustomIntList[:]

        # assign value to an item
        self.CustomIntList[0] = 5

        #
        def GetLengthOfAnArray() -> int: return len(newList)

        #
        def AddItemToAnArray(num: int) -> None: newList.append(num)

        #

    #   [SET]   convert set to list
    def ConvertSetToList(self) -> list[int]:
        return list(self.CustomIntSet)

    #   [SET]   look for item in Set
    def ItemLookUpInSet(self, lookFor: int) -> bool:
        isExist: bool = lookFor in self.CustomIntSet
        return isExist

    #   [SET]   add item to set
    def AddItemToSet(self, item: int) -> None:
        self.CustomIntSet.add(item)
        print(self.CustomIntSet)

    #   [SET]   copy items in set
    def CopyItemInSet(self) -> set[int]:
        return self.CustomIntSet.copy()

    #   [SET]   remove item in set
    def DeleteItemInSet(self, item: int) -> set[int]:
        self.CustomIntSet.remove(item)
        return self.CustomIntSet

    @staticmethod
    def DeconstructExample() -> None:
        # deconstruct array
        x, y, z = [1, 2, 3]

        # deconstruct tuple
        a, b, c = (5, 6, 7)

    def PrintTheDic(self) -> None:
        dic = self.ExampleDic.items()
        for key, value in dic:
            print(key, value)

        anotherDic = self.ExampleDic
        for kvp in anotherDic:
            print(kvp, anotherDic[kvp])

    #
    def FillingDic(self) -> None:
        #   prepare values
        values = [1, 2, 3, 4, 5]
        keys = ["a", "b", "c", "d", "e"]

        #   insert into dictionary
        for value in values:
            self.EmptyIntDic[keys] = value

        #   print dic
        print(self.EmptyIntDic)

    #
    def AcceptParam(self, dic: dict[str, str]) -> dict[str, str]:
        for key in dic:
            if (type(key).__name__ != "str"):
                raise Exception("key must be string")
            if (type(dic[key]).__name__ != "str"):
                raise Exception(
                    "value for key '{}' must be string".format(key))
            print(key, dic[key])
        return dic

    # List, an array, with everything
    @staticmethod
    def ListComprehensionExample() -> None:
        # list between 1 and 10
        listComp1 = [num for num in range(1, 10 + 1)]

        # list between 1 and 10 with each number of its own square
        listComp2 = [num*num for num in range(1, 10 + 1)]

        # list between 1 and 10 with each number of its own square and show only even number
        listComp3 = [num*num for num in range(1, 10 + 1) if num % 2]

        #
        print({'listComp1': listComp1, 'listComp2': listComp2, 'listComp3': listComp3})

    # Set, an array, with no duplicated item
    @staticmethod
    def SetComprehensionExample() -> None:
        # generate a set between 1 and 10
        setComp1 = {num for num in range(1, 10 + 1)}

        # generate a set between 1 and 10 with each number of its own square
        setComp2 = {num*num for num in range(1, 10 + 1)}

        # generate a set between 1 and 10 with each number of its own square and show only even number
        setComp3 = {num*num for num in range(1, 10 + 1) if num % 2}

        #
        print({'setComp1': setComp1, 'setComp2': setComp2, 'setComp3': setComp3})

    @staticmethod
    # Dictionary, a list of key-value-pair
    def DictionaryComprehensionExample() -> None:
        # a base dictionary
        dic = {'a': 1, 'b': 2, 'c': 3}

        # get a dictionary with value of is 2 times of the original value, and show only the value is even
        dicComp1 = {k: v * 2 for k, v in dic.items() if v % 2}

        #
        dicComp2 = {num: num * 2 for num in [1, 2, 3]}

        #
        print({'dicComp1': dicComp1, 'dicComp2': dicComp2})
