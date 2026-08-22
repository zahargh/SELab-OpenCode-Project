# Agent Instructions — 01-OOD-Principles-Without

## Project Overview
Python store/order system demonstrating OOD principles (intentionally violating SOLID for teaching purposes). Single package `store/` with 7 modules.

## Running the Project
```bash
python -m store.main
# or
python store/main.py
```

## Key Files
- `store/models.py` — dataclasses: Customer, OrderItem, Order, BundleOrder
- `store/payment.py` — PaymentProcessor with if/elif chain for credit_card/paypal/bitcoin
- `store/pricing.py` — DiscountCalculator (VIP 20%, bulk 10%, WELCOME10 coupon 10%)
- `store/notification.py` — NotificationService + SmsOnlyNotifier (LSP violation)
- `store/storage.py` — MySqlDatabase (in-memory dict)
- `store/order_service.py` — OrderService orchestrates full checkout flow
- `store/main.py` — demo entrypoint

## Constraints (from lab exercise)
**Do not refactor.** The if/elif chain in `PaymentProcessor.process()` must stay. To add "cash" payment:
1. Add `elif method == "cash":` branch in `payment.py:process()` returning `"paid_by_cash:{amount:.2f}"`
2. Add demo order with `payment_method="cash"` in `main.py`

## No Tooling Configured
- No pyproject.toml / setup.py / requirements.txt
- No pytest, no lint, no typecheck
- No CI workflows

## Git
- Repo root: `E:\SE-Lab-Ex2\01-OOD-Principles-Without`
- .gitignore excludes macOS/VSCode artifacts only

## Why no refactor here
This is Phase 1 of a SOLID-principles lab exercise. The goal is to measure
how much change a poorly-designed codebase requires for a new feature,
before comparing it to a refactored version in Phase 2.