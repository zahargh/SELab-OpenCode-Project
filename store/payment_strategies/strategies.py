from store.models import Order
from store.interfaces import IPaymentStrategy


class CreditCardPaymentStrategy(IPaymentStrategy):
    @property
    def method_name(self) -> str:
        return "credit_card"

    def pay(self, order: Order, amount: float) -> str:
        card = order.customer.credit_card
        print(f"[payment] Charging card {card} {amount:.2f}")
        return f"paid_by_credit_card:{amount:.2f}"


class PayPalPaymentStrategy(IPaymentStrategy):
    @property
    def method_name(self) -> str:
        return "paypal"

    def pay(self, order: Order, amount: float) -> str:
        email = order.customer.email
        print(f"[payment] Charging PayPal {email} {amount:.2f}")
        return f"paid_by_paypal:{amount:.2f}"


class BitcoinPaymentStrategy(IPaymentStrategy):
    @property
    def method_name(self) -> str:
        return "bitcoin"

    def pay(self, order: Order, amount: float) -> str:
        address = order.customer.bitcoin_address
        print(f"[payment] Charging BTC {address} {amount:.2f}")
        return f"paid_by_bitcoin:{amount:.2f}"


class CashPaymentStrategy(IPaymentStrategy):
    @property
    def method_name(self) -> str:
        return "cash"

    def pay(self, order: Order, amount: float) -> str:
        print(f"[payment] Cash payment {amount:.2f}")
        return f"paid_by_cash:{amount:.2f}"