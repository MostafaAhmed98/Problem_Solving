class StandardPackageDelivery:
    def __init__(self, sender_address, receiver_address, weight_in_kg, price_per_kg):
        self.weight_in_kg = weight_in_kg
        self.price_per_kg = price_per_kg
        self.cost = weight_in_kg * price_per_kg
        self.sender_address = sender_address
        self.receiver_address = receiver_address


class TwoDaysPackage(StandardPackageDelivery):
    def __init__(self, sender_address, receiver_address, weight_in_kg, price_per_kg, fixed_fee):
        super().__init__(sender_address, receiver_address, weight_in_kg, price_per_kg)
        self.fixed_fees = fixed_fee
        self.cost_with_fixed_cost = self.cost + self.fixed_fees

    def cost_of_the_package(self):
        return print(f'The cost of the Package will be the normal cost {self.cost} + '
                     f'the fixed fee {self.fixed_fees}, so the total cost will be {self.cost_with_fixed_cost}')


class HeavyPackage(StandardPackageDelivery):
    MAX_WEIGHT = 100

    def __init__(self, sender_address, receiver_address, weight_in_kg, price_per_kg):
        super().__init__(sender_address, receiver_address, weight_in_kg, price_per_kg)
        self.penalty = 0

    def cost_of_the_package(self):
        if self.weight_in_kg > self.MAX_WEIGHT:
            self.penalty = (self.weight_in_kg - self.MAX_WEIGHT) * self.price_per_kg

        return print(f'The cost of the Package will be the normal cost {self.cost} + '
                     f'the penalty fee {self.penalty}, so the total cost will be {self.cost + self.penalty}')




if __name__ == '__main__':
    Ipad = TwoDaysPackage("Fawry Company, 1 Gad el Haq street - Cairo",
                          "Mostafa Ahmed, 47 Mohamed MEtwally el Sharawy street - Giza",
                          50, 2, 20)
    Ipad.cost_of_the_package()

    Bed = HeavyPackage("Mffco Company, 1 Gad el Haq street - Cairo",
                       "Mostafa Ahmed, 47 Mohamed Metwally el Sharawy street - Giza",
                       200, 2)
    Bed.cost_of_the_package()
