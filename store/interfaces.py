from abc import ABC, abstractmethod
from typing import List, Optional
from store.models import Order, Customer


# ============================================================
# Payment (OCP - Strategy Pattern)
# ============================================================

class IPaymentProcessor(ABC):
    @abstractmethod
    def process(self, order: Order, amount: float) -> str:
        pass


class IPaymentStrategy(ABC):
    @abstractmethod
    def pay(self, order: Order, amount: float) -> str:
        pass

    @property
    @abstractmethod
    def method_name(self) -> str:
        pass


# ============================================================
# Pricing (OCP - Strategy/Composite Pattern)
# ============================================================

class IDiscountRule(ABC):
    @abstractmethod
    def applies_to(self, order: Order) -> bool:
        pass

    @abstractmethod
    def calculate_discount(self, order: Order) -> float:
        pass


class IDiscountCalculator(ABC):
    @abstractmethod
    def calculate(self, order: Order) -> float:
        pass

    @abstractmethod
    def add_rule(self, rule: IDiscountRule) -> None:
        pass


# ============================================================
# Notification (ISP - Interface Segregation)
# ============================================================

class IEmailNotifier(ABC):
    @abstractmethod
    def send_email(self, customer: Customer, message: str) -> None:
        pass


class ISmsNotifier(ABC):
    @abstractmethod
    def send_sms(self, customer: Customer, message: str) -> None:
        pass


class IPushNotifier(ABC):
    @abstractmethod
    def send_push(self, customer: Customer, message: str) -> None:
        pass


class INotificationService(ABC):
    @abstractmethod
    def notify(self, customer: Customer, message: str) -> None:
        pass


# ============================================================
# Storage (DIP - Repository Pattern)
# ============================================================

class IOrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order) -> None:
        pass

    @abstractmethod
    def load(self, order_id: int) -> Optional[Order]:
        pass

    @abstractmethod
    def exists(self, order_id: int) -> bool:
        pass


# ============================================================
# Order Service Components (SRP)
# ============================================================

class IOrderValidator(ABC):
    @abstractmethod
    def validate(self, order: Order) -> None:
        pass


class IPricingService(ABC):
    @abstractmethod
    def calculate_total(self, order: Order) -> float:
        pass


class IPaymentService(ABC):
    @abstractmethod
    def charge(self, order: Order, amount: float) -> str:
        pass


class IOrderPersistenceService(ABC):
    @abstractmethod
    def persist(self, order: Order) -> None:
        pass


class IOrderNotificationService(ABC):
    @abstractmethod
    def send_confirmation(self, order: Order, total: float, receipt: str) -> None:
        pass


class IReceiptPrinter(ABC):
    @abstractmethod
    def print_receipt(self, order: Order, subtotal: float, discount: float,
                      shipping: float, total: float, receipt: str) -> None:
        pass


class IOrderOrchestrator(ABC):
    @abstractmethod
    def process_order(self, order: Order, notify: bool = True) -> Order:
        pass