from typing import Optional
from store.models import Order
from store.interfaces import IPaymentProcessor
from store.payment_strategies.factory import PaymentStrategyFactory


class PaymentProcessor(IPaymentProcessor):
    def __init__(self, factory: Optional[PaymentStrategyFactory] = None):
        self._factory = factory or PaymentStrategyFactory()

    def process(self, order: Order, amount: float) -> str:
        strategy = self._factory.get_strategy(order.payment_method)
        return strategy.pay(order, amount)