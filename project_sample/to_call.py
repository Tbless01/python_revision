from project_sample.Product import Product
from project_sample.oop import Point


class Pointer:
    # todo ":Point" mean ure specifying its type
    p2: Point = Point(7, 9)
    p2.draw()
    p2.__setter__(2)
    print(p2.__getter__())
    print(p2)

    print(p2.default_color)
    print(Point.default_color)

    #  todo   how to locate where a particular method is coming from
    print(isinstance(p2, Point))

    ju: Product = Product(3)
    # ju.__setter__(34)
    # print(ju.__getter__())

    print(ju)