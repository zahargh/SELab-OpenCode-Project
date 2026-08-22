from store.models import Order, PricingBreakdown
from store.interfaces import IPricingService, IDiscountCalculator


class PricingService(IPricingService):
    def __init__(self, discount_calculator: IDiscountCalculator):
        self._discount_calculator = discount_calculator

    def calculate_total(self, order: Order) -> PricingBreakdown:
        subtotal = order.subtotal
        discount = self._discount_calculator.calculate(order)
        shipping = 5.0 if subtotal < 100 else 0.0
        total = round(subtotal - discount + shipping, 2)
        return PricingBreakdown(
            subtotal=subtotal,
            discount=discount,
            shipping=shipping,
            total=total,
        )