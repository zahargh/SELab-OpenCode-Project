from store.models import Order
from store.interfaces import IPaymentService, IPaymentProcessor


class PaymentService(IPaymentService):
    def __init__(self, payment_processor: IPaymentProcessor):
        self._payment_processor = payment_processor

    def charge(self, order: Order, amount: float) -> str:
        return self._payment_processor.process(order, amount)