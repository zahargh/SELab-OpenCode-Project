from store.models import Order, PricingBreakdown
from store.interfaces import (
    IOrderOrchestrator,
    IOrderValidator,
    IPricingService,
    IPaymentService,
    IOrderPersistenceService,
    IOrderNotificationService,
    IReceiptPrinter,
)


class OrderOrchestrator(IOrderOrchestrator):
    def __init__(
        self,
        validator: IOrderValidator,
        pricing: IPricingService,
        payment: IPaymentService,
        persistence: IOrderPersistenceService,
        notification: IOrderNotificationService,
        printer: IReceiptPrinter,
    ):
        self._validator = validator
        self._pricing = pricing
        self._payment = payment
        self._persistence = persistence
        self._notification = notification
        self._printer = printer

    def process_order(self, order: Order, notify: bool = True) -> Order:
        # 1. validate
        self._validator.validate(order)

        # 2. calculate pricing
        breakdown: PricingBreakdown = self._pricing.calculate_total(order)

        # 3. charge payment
        receipt = self._payment.charge(order, breakdown.total)

        # 4. persist
        self._persistence.persist(order)

        # 5. notify (conditional)
        if notify:
            self._notification.send_confirmation(order, breakdown.total, receipt)

        # 6. print receipt
        self._printer.print_receipt(order, breakdown, receipt)

        return order