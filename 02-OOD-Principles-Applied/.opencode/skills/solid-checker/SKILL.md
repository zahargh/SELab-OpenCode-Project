---
name: solid-checker
description: Use when the user asks to check, review, analyze, or refactor code for SOLID principle violations (SRP, OCP, LSP, ISP, DIP) in Python projects. Identifies violations, explains why, proposes a specific refactor, and applies changes only after explicit user approval.
---

# SOLID Checker

## هدف
شناسایی نقض هر یک از پنج اصل SOLID در کد پایتون پروژه، ارائه دلیل مبتنی بر کد واقعی برای هر نقض، پیشنهاد یک راهکار Refactoring مشخص، و اعمال تغییرات فقط پس از تایید صریح کاربر.

## دستورالعمل تحلیل
- SRP: آیا یک کلاس/متد بیش از یک دلیل برای تغییر دارد؟
- OCP: آیا افزودن رفتار جدید نیازمند تغییر مستقیم در کد موجود است؟
- LSP: آیا زیرکلاس‌ها می‌توانند بدون تغییر رفتار قابل‌مشاهده جایگزین کلاس پایه شوند؟
- ISP: آیا کلاینت‌ها مجبورند به متدهایی وابسته باشند که استفاده نمی‌کنند؟
- DIP: آیا ماژول‌های سطح بالا مستقیماً به پیاده‌سازی‌های concrete وابسته‌اند؟

## قالب خروجی
اصل: [نام اصل]
محل: [نام فایل و کلاس/متد]
علت: [توضیح مبتنی بر خطوط واقعی کد]
راهکار پیشنهادی: [نام الگوی طراحی یا تکنیک]

در پایان هر مورد بپرس: "آیا این تغییر اعمال شود؟ (بله/خیر)"

## قید مهم
هرگز بدون پاسخ صریح "بله" از کاربر، هیچ فایلی را ویرایش نکن.