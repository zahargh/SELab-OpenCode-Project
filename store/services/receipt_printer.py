from store.models import Order, PricingBreakdown
from store.interfaces import IReceiptPrinter


class ReceiptPrinter(IReceiptPrinter):
    def print_receipt(
        self,
        order: Order,
        breakdown: PricingBreakdown,
        receipt: str,
    ) -> None:
        print(f"--- Receipt for order {order.id} ---")
        for item in order.items:
            print(f"  {item.name:20s} x{item.quantity}  ${item.line_total:.2f}")
        print(f"  Subtotal    ${breakdown.subtotal:.2f}")
        print(f"  Discount   -${breakdown.discount:.2f}")
        print(f"  Shipping    ${breakdown.shipping:.2f}")
        print(f"  TOTAL       ${breakdown.total:.2f}")
        print(f"  Payment     {receipt}")