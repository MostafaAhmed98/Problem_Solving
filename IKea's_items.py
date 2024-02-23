class Items:
    def __init__(self, name, id, price):
        self.name = name
        self.id = id
        self.price = price


class ComplexItems(Items):
    def __init__(self, name, id, **kwargs):
        super().__init__(name, id, kwargs)
        self.items = {}
        for key, value in kwargs.items():
            self.items[key] = value

    def complex_item_price(self):
        sum_value = 0
        for key, value in self.items.items():
            print(f'the price of {key} of the {self.name} is {value}')
            sum_value += value
        return print(f"The whole cost for the {self.name} is {sum_value}")


class SimpleItems(Items):
    pass


if __name__ == '__main__':
    chair = ComplexItems("Chair", 2, left_leg=70, right_leg=90, back_bone=100)
    chair.complex_item_price()
