from typing import Optional
from store.interfaces import INotificationService
from store.notifiers import EmailNotifier, SmsNotifier, PushNotifier, CompositeNotifier


class NotificationService(INotificationService):
    def __init__(self, notifier: Optional[CompositeNotifier] = None):
        self._notifier = notifier or CompositeNotifier(
            email_notifier=EmailNotifier(),
            sms_notifier=SmsNotifier(),
        )

    def notify(self, customer, message: str) -> None:
        self._notifier.notify(customer, message)

    # Backward compatibility
    def send_email(self, customer, message: str) -> None:
        EmailNotifier().send_email(customer, message)

    def send_sms(self, customer, message: str) -> None:
        SmsNotifier().send_sms(customer, message)

    def send_push(self, customer, message: str) -> None:
        PushNotifier().send_push(customer, message)