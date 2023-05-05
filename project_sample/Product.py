class Product:

    def __init__(self, price):
        self.price = price

    # def __setter__(self, price):
    #     if price < 0:
    #         raise ValueError("Price cannot be negative")
    #     self.price = price
    #
    # def __getter__(self):
    #     return self.price
    # todo another way to write getter setter

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price

    def __str__(self):
        return f"{self.__price}"
