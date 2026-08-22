from typing import Optional
from store.models import Order
from store.interfaces import IOrderRepository


class InMemoryRepository(IOrderRepository):
    """In-memory implementation of Order Repository"""
    
    def __init__(self):
        self._orders = {}

    def save(self, order: Order) -> None:
        self._orders[order.id] = order

    def load(self, order_id: int) -> Optional[Order]:
        return self._orders.get(order_id)

    def exists(self, order_id: int) -> bool:
        return order_id in self._orders

    def clear(self) -> None:
        self._orders.clear()

    def count(self) -> int:
        return len(self._orders)