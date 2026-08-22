from store.models import Order
from store.interfaces import IOrderPersistenceService, IOrderRepository


class OrderPersistenceService(IOrderPersistenceService):
    def __init__(self, repository: IOrderRepository):
        self._repository = repository

    def persist(self, order: Order) -> None:
        order.status = "paid"
        self._repository.save(order)