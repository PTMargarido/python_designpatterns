import math

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.__x = x
        self.__y = y

    def __str__(self):
        return "Point: {0}, {1}".format(self.__x, self.__y)

    @classmethod
    def NewCartesian(cls, x: float, y: float):
        return cls(x, y)

    @staticmethod
    def NewPolar(r: float, theta: float):
        return Point(r * math.cos(theta), r * math.sin(theta))


if __name__ == "__main__":
    p1 = Point.NewCartesian(5.0, 6.0)
    p2 = Point.NewPolar(2.0, math.pi)
    print(p1)
    print(p2)
