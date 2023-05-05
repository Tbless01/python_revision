class Point:

    # todo default_colour is available through the name of the class and instance of a class
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"The point is from {self.x} to {self.y}"

    def draw(self):
        print(f"drawing....from {self.x} to {self.y}")

    def __setter__(self, x):
        self.x = x * 6

    def __getter__(self):
        return self.x
# p1 = Point()
# p1.draw()
