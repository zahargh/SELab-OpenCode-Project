from typing import List, Optional
from store.models import Order
from store.interfaces import IDiscountCalculator, IDiscountRule


class DiscountCalculator(IDiscountCalculator):
    def __init__(self, rules: Optional[List[IDiscountRule]] = None):
        self._rules = rules or []

    def calculate(self, order: Order) -> float:
        for rule in self._rules:
            if rule.applies_to(order):
                return rule.calculate_discount(order)
        return 0.0

    def add_rule(self, rule: IDiscountRule) -> None:
        self._rules.append(rule)

    @property
    def rules(self) -> List[IDiscountRule]:
        return self._rules