from store.models import Customer
from store.interfaces import IEmailNotifier


class EmailNotifier(IEmailNotifier):
    def send_email(self, customer: Customer, message: str) -> None:
        print(f"[email] to {customer.email}: {message}")