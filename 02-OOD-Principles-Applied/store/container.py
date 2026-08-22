from store.payment_strategies.factory import PaymentStrategyFactory
from store.payment import PaymentProcessor
from store.pricing_rules.calculator import DiscountCalculator as DefaultDiscountCalculator
from store.pricing_rules.rules import VIPDiscountRule, BulkDiscountRule, CouponDiscountRule
from store.pricing import DiscountCalculator
from store.notifiers import EmailNotifier, SmsNotifier, PushNotifier, CompositeNotifier
from store.notification import NotificationService
from store.repositories import MySqlRepository
from store.storage import MySqlDatabase
from store.services import (
    OrderValidator,
    PricingService,
    PaymentService,
    OrderPersistenceService,
    OrderNotificationService,
    ReceiptPrinter,
    OrderOrchestrator,
)


class Container:
    def __init__(self):
        # Payment
        self._payment_factory = PaymentStrategyFactory()
        self._payment_processor = PaymentProcessor(self._payment_factory)

        # Pricing
        self._discount_calculator = DefaultDiscountCalculator([
            VIPDiscountRule(),
            BulkDiscountRule(),
            CouponDiscountRule(),
        ])
        self._discount_calculator_facade = DiscountCalculator(self._discount_calculator)

        # Notification (single instance used by both facade and external access)
        self._composite_notifier = CompositeNotifier(
            email_notifier=EmailNotifier(),
            sms_notifier=SmsNotifier(),
        )
        self._notification_service = NotificationService(self._composite_notifier)

        # Storage (single repository instance)
        self._repository = MySqlRepository()
        self._database = MySqlDatabase(self._repository)

        # Services (SRP)
        self._validator = OrderValidator()
        self._pricing_service = PricingService(self._discount_calculator_facade)
        self._payment_service = PaymentService(self._payment_processor)
        self._persistence_service = OrderPersistenceService(self._repository)
        self._notification_service_facade = OrderNotificationService(self._notification_service)
        self._receipt_printer = ReceiptPrinter()

        # Orchestrator (main entry point)
        self._orchestrator = OrderOrchestrator(
            validator=self._validator,
            pricing=self._pricing_service,
            payment=self._payment_service,
            persistence=self._persistence_service,
            notification=self._notification_service_facade,
            printer=self._receipt_printer,
        )

    @property
    def orchestrator(self) -> OrderOrchestrator:
        return self._orchestrator

    # Expose actual shared instances for testing
    @property
    def payment_processor(self) -> PaymentProcessor:
        return self._payment_processor

    @property
    def discount_calculator(self) -> DiscountCalculator:
        return self._discount_calculator_facade

    @property
    def notification_service(self) -> NotificationService:
        return self._notification_service

    @property
    def database(self) -> MySqlDatabase:
        return self._database

    @property
    def repository(self) -> MySqlRepository:
        return self._repository