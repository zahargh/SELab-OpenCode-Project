from store.models import Customer
from store.interfaces import ISmsNotifier


class SmsNotifier(ISmsNotifier):
    def send_sms(self, customer: Customer, message: str) -> None:
        print(f"[sms] to {customer.phone}: {message}")