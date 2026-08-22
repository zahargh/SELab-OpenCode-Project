from store.models import Order
from store.interfaces import IOrderRepository
from store.repositories import MySqlRepository


class MySqlDatabase(IOrderRepository):
    def __init__(self, connection_string: str = "mysql://localhost/store"):
        self._repository = MySqlRepository(connection_string)

    def save_order(self, order) -> None:
        self._repository.save(order)

    def load_order(self, order_id: int):
        return self._repository.load(order_id)

    # IOrderRepository implementation
    def save(self, order: Order) -> None:
        self._repository.save(order)

    def load(self, order_id: int):
        return self._repository.load(order_id)

    def exists(self, order_id: int) -> bool:
        return self._repository.exists(order_id)