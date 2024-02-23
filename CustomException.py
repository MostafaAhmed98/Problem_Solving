class ProjectBaseException(BaseException):
    pass


class NegativePaymentException(ProjectBaseException):
    def __init__(self, money, message='Paid amount must be positive'):
        self.money = money
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.money} amount cause error \n {self.message}"


class AgeNotReal(ProjectBaseException):
    def __init__(self, age, message="Age is not real"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        if self.age < 0 or self.age > 100:
            return f"Your Age is not real"


if __name__ == '__main__':
    raise AgeNotReal(-9)
    #raise NegativePaymentException(-20)
