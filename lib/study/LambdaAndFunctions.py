from functools import reduce


class LambdaAndFunctionExample:

    #   Item Multiplier
    def ItemMultiplier(self, arr: list[int]) -> list[int]:
        multiplyArray = map(lambda item: item * 2, arr)
        return list(multiplyArray)

    #   Item Filter Odd Only
    def ItemFilterOddOnly(self, arr: list[int]) -> list[int]:
        oddOnly = filter(lambda item: item % 2, arr)
        return list(oddOnly)

    #   Reduce an array to a value
    def ItemReducer(self, arr: list[int]) -> int:
        reduceExample: int = reduce(lambda acc, item: acc + item, arr, 0)
        return reduceExample

    #   Sort array of int
    def SquareLambda(self, arr: list[int]) -> list[int]:
        squareArr: list[int] = list(map(lambda item: item * item, arr))
        return squareArr

    #   Zipper function
    @staticmethod
    def ZipperFunction() -> list[tuple[int, int, int]]:
        zipExample = zip(range(5), range(3), range(4))
        return zipExample

    #   Sort array of tuple
    def SortTuple(self, arrTuple: list[tuple[int]]) -> list[tuple[int]]:
        sortedTuple: list[tuple[int]] = list(
            sorted(arrTuple, key=lambda tup: tup[1], reverse=False))
        return sortedTuple
