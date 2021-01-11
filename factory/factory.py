import math

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.__x = x
        self.__y = y

    def __str__(self):
        return "Point: {0}, {1}".format(self.__x, self.__y)


class PointFactory:

    def NewCartesian(self, x: float, y: float) -> Point:
        return Point(x, y)

    def NewPolar(self, r: float, theta: float) -> Point:
        return Point(r * math.cos(theta), r * math.sin(theta))


if __name__ == "__main__":
    p1f = PointFactory()
    p1 = p1f.NewCartesian(5.0, 6.0)
    p2 = p1f.NewPolar(2.0, math.pi)
    print(p1)
    print(p2)
