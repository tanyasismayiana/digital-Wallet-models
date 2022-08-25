from re import A
from time import clock_settime
from django.contrib import admin

# Register your models here.
from .models import Account, Currency, Customer, Third_party, Wallet, Notification, Transaction, Card, Receipt, Loan, Reward


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "address")
    search_fields = ("first_name", "last_name", "address")


admin.site.register(Customer, CustomerAdmin)


class WalletAdmin(admin.ModelAdmin):
    list_display = ("Balance", "customer", "type", "active")
    search_fields = ("Balance", "customer", "type", "active")


admin.site.register(Wallet, WalletAdmin)


class AccountAdmin(admin.ModelAdmin):
    list_display = ("account_type", "account_name")
    search_fields = ("account_type", "account_name")


admin.site.register(Account, AccountAdmin)


class NotificatonAdmin(admin.ModelAdmin):
    list_display = ("Unique_identifier", "Sent_on", "Delivered_on")
    search_fields = ("Unique_identifier", "Sent_on", "Delivered_on")


admin.site.register(Notification, NotificatonAdmin)


class TrasactionAdmin(admin.ModelAdmin):
    list_display = ("transaction_type", "account_origin")
    search_fields = ("transaction_type", "account_origin")


admin.site.register(Transaction, TrasactionAdmin)


class CardAdmin(admin.ModelAdmin):
    list_display = ("date_Issued", "card_status", "issuer")
    search_fields = ("date_Issued", "card_status", "issuer")


admin.site.register(Card, CardAdmin)


class ReceiptAdmin(admin.ModelAdmin):
    list_display = ("date", "transaction")
    search_fields = ("date", "transaction")


admin.site.register(Receipt, ReceiptAdmin)


class LoanAdmin(admin.ModelAdmin):
    list_display = ("loan_type", "amount")
    search_fields = ("loan_type", "amount")


admin.site.register(Loan, LoanAdmin)


class RewardAdmin(admin.ModelAdmin):
    list_display = ("wallet", "point", "date")
    search_fields = ("wallet", "point", "date")


admin.site.register(Reward, ReceiptAdmin)


class Third_partyAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone_number")
    search_fields = ("full_name", "email")


admin.site.register(Third_party, Third_partyAdmin)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("symbol", "amount")
    search_fields = ("symbol", "amount")


admin.site.register(Currency, CurrencyAdmin)
