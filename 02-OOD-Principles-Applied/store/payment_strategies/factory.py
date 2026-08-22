from typing import Dict
from store.interfaces import IPaymentStrategy
from store.payment_strategies.strategies import (
    CreditCardPaymentStrategy,
    PayPalPaymentStrategy,
    BitcoinPaymentStrategy,
    CashPaymentStrategy,
)


class PaymentStrategyFactory:
    def __init__(self):
        self._strategies: Dict[str, IPaymentStrategy] = {
            "credit_card": CreditCardPaymentStrategy(),
            "paypal": PayPalPaymentStrategy(),
            "bitcoin": BitcoinPaymentStrategy(),
            "cash": CashPaymentStrategy(),
        }

    def get_strategy(self, method: str) -> IPaymentStrategy:
        strategy = self._strategies.get(method)
        if not strategy:
            raise ValueError(f"Unknown payment method: {method!r}")
        return strategy

    def register_strategy(self, method: str, strategy: IPaymentStrategy) -> None:
        self._strategies[method] = strategy

    @property
    def supported_methods(self) -> list[str]:
        return list(self._strategies.keys())