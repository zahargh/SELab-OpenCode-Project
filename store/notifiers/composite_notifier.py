from typing import Optional
from store.models import Customer
from store.interfaces import INotificationService, IEmailNotifier, ISmsNotifier, IPushNotifier


class CompositeNotifier(INotificationService):
    def __init__(
        self,
        email_notifier: Optional[IEmailNotifier] = None,
        sms_notifier: Optional[ISmsNotifier] = None,
        push_notifier: Optional[IPushNotifier] = None,
    ):
        self._email = email_notifier
        self._sms = sms_notifier
        self._push = push_notifier

    def notify(self, customer: Customer, message: str) -> None:
        if self._email and customer.email:
            self._email.send_email(customer, message)
        if self._sms and customer.phone:
            self._sms.send_sms(customer, message)
        if self._push:
            self._push.send_push(customer, message)