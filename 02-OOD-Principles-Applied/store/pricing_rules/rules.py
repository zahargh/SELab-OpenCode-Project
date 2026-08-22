from store.models import Order
from store.interfaces import IDiscountRule


class VIPDiscountRule(IDiscountRule):
    def applies_to(self, order: Order) -> bool:
        return order.customer.is_vip

    def calculate_discount(self, order: Order) -> float:
        return round(order.subtotal * 0.20, 2)


class BulkDiscountRule(IDiscountRule):
    def __init__(self, min_items: int = 10, discount_rate: float = 0.10):
        self._min_items = min_items
        self._discount_rate = discount_rate

    def applies_to(self, order: Order) -> bool:
        return order.item_count >= self._min_items

    def calculate_discount(self, order: Order) -> float:
        return round(order.subtotal * self._discount_rate, 2)


class CouponDiscountRule(IDiscountRule):
    def __init__(self, coupon_code: str = "WELCOME10", discount_rate: float = 0.10):
        self._coupon_code = coupon_code
        self._discount_rate = discount_rate

    def applies_to(self, order: Order) -> bool:
        return self._coupon_code in order.coupons

    def calculate_discount(self, order: Order) -> float:
        return round(order.subtotal * self._discount_rate, 2)