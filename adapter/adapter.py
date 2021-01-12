import math


class Cylinder:

    def __init__(self, radius: float):
        self.__s = radius

    def get_width(self) -> float:
        return self.__s


class Cube:

    def __init__(self, side: float):
        self.__s = side

    def get_width(self) -> float:
        return self.__s


class RoundHole:

    def __init__(self, radius: float):
        self.__r = radius

    def fit_in(self, obj: Cylinder) -> bool:
        return obj.get_width() <= self.__r


class CubeAdapter(Cylinder):

    def __init__(self, cube: Cube):
        self.__c = cube

    def get_width(self) -> float:
        return self.__c.get_width() * math.sqrt(2)


if __name__ == "__main__":

    a = RoundHole(5.0)
    sqa = Cube(2)

    ca = CubeAdapter(sqa)

    print(a.fit_in(ca))
