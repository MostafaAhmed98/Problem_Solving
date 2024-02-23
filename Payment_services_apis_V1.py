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
        self.name = None
        self.address = None


class StripeCardInfo:
    def __init__(self, id=None, expire_date=None):
        self.id = id
        self.expire_date = expire_date


class StripePaymentAPI:
    @staticmethod
    def withdraw_money(user_info, card_info, money):
        print(f"StripePaymentAPI request")
        return True


class PaymentProcessor:

    def payment_with_paypal(self, name, address, id, expire_date, ccv, money):
        card_info = PayPalCreditCard(name, address, id, expire_date, ccv)
        payment = PayPalOnlinePaymentAPI(card_info)
        payment.pay_money(money)

    def payment_with_stripe(self, name, address, id, expire_date, money):
        user_info = StripUserInfo(name, address)
        card_info = StripeCardInfo(id, expire_date)
        payment = StripePaymentAPI()
        payment.withdraw_money(user_info, card_info, money)


if __name__ == '__main__':
    pay = PaymentProcessor()
    pay.payment_with_paypal("Mostafa", "cairo", 50, 2024, 586, 100)
    pay.payment_with_stripe("Mostafa Ahmed", "Giza", 50, 2025, 500)
