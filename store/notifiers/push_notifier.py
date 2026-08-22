from store.models import Customer
from store.interfaces import IPushNotifier


class PushNotifier(IPushNotifier):
    def send_push(self, customer: Customer, message: str) -> None:
        print(f"[push] to {customer.name}: {message}")