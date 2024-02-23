from abc import ABC, abstractmethod


class PayPalCreditCard:
    def __init__(self, name=None, address=None, id=None, expire_date=None, ccv=None):
        self.name = name
        self.address = address
        self.id = id
        self.expire_date = expire_date
        self.ccv = ccv


class PayPalOnlinePaymentAPI:
    def __init__(self, card_info: PayPalCreditCard = None):
        self.card_info = None

    def pay_money(self, money):
        print(f'PayPalOnlinePaymentAPI request')
        print(self.card_info)


class StripUserInfo:
    def __init__(self, name=None, address=None):
        self.name = name
        self.address = address


class StripeCardInfo:
    def __init__(self, id=None, expire_date=None):
        self.id = id
        self.expire_date = expire_date


class StripePaymentAPI:
    @staticmethod
    def withdraw_money(user_info, card_info, money):
        print(f"StripePaymentAPI request")
        return True


class IPayment(ABC):
    @abstractmethod
    def user_info(self, name, address):
        pass

    @abstractmethod
    def card_info(self, id, expire_date, ccv):
        pass

    @abstractmethod
    def make_payment(self, money):
        pass


class PaymentWithPayPal(IPayment):
    def __init__(self):
        self.paypal = PayPalOnlinePaymentAPI()
        self.card = PayPalCreditCard()

    def user_info(self, name, address):
        self.card.name = name
        self.card.address = address

    def card_info(self, id, expire_date, ccv):
        self.card.id = id
        self.card.expire_date = expire_date
        self.card.ccv = ccv

    def make_payment(self, money):
        return self.paypal.pay_money(money)


class PaymentWithStripe(IPayment):
    def __init__(self):
        self.user = StripUserInfo()
        self.card = StripeCardInfo()
        self.stripe = StripePaymentAPI()

    def user_info(self, name, address):
        self.user.name = name
        self.user.address = address

    def card_info(self, id, expire_date, ccv=None):
        self.card.id = id
        self.card.expire_date = expire_date

    def make_payment(self, money):
        return self.stripe.withdraw_money(self.user, self.card, money)


if __name__ == '__main__':
    payment_with_paypal = PaymentWithPayPal()
    payment_with_paypal.user_info("Mostafa", "Cairo")
    payment_with_paypal.card_info(50, 2025, 586)
    payment_with_paypal.make_payment(80)
    payment_with_stripe = PaymentWithStripe()
    payment_with_stripe.user_info("Mostafa", "Cairo")
    payment_with_stripe.card_info(60, 2024)
    payment_with_stripe.make_payment(80)
