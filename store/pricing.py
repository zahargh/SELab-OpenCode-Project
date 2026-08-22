from typing import Optional
from store.models import Order
from store.interfaces import IDiscountCalculator
from store.pricing_rules.rules import VIPDiscountRule, BulkDiscountRule, CouponDiscountRule
from store.pricing_rules.calculator import DiscountCalculator as DefaultDiscountCalculator


class DiscountCalculator(IDiscountCalculator):
    def __init__(self, calculator: Optional[DefaultDiscountCalculator] = None):
        self._calculator = calculator or DefaultDiscountCalculator([
            VIPDiscountRule(),
            BulkDiscountRule(),
            CouponDiscountRule(),
        ])

    def calculate(self, order: Order) -> float:
        return self._calculator.calculate(order)

    def add_rule(self, rule) -> None:
        self._calculator.add_rule(rule)