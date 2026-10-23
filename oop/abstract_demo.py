from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self):
        pass

class RyanPay(PaymentGateway):
    def pay(self):
        print("Paying Using RyanPay")

class RazorPay(PaymentGateway):
    def pay(self):
        print("paying using RazorPay..")

class Purchase:

    def __init__(self, gateway):
        self.gateway = gateway

    def checkout(self):
        print("Checking out...")

        self.gateway.pay()

gateway1 = RazorPay()
gateway2 = RyanPay()
purchase = Purchase(gateway2)

purchase.checkout()