from store.models import Order
from store.interfaces import IOrderNotificationService, INotificationService


class OrderNotificationService(IOrderNotificationService):
    def __init__(self, notification_service: INotificationService):
        self._notification_service = notification_service

    def send_confirmation(self, order: Order, total: float, receipt: str) -> None:
        message = f"Order {order.id} total ${total:.2f} ({receipt})"
        self._notification_service.notify(order.customer, message)