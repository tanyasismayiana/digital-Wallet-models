from django.contrib import admin

# Register your models here.
from .models import Account, Customer, Wallet,Notification,Transaction,Card,Receipt,Loan,Reward
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","address")
    search_fields = ("first_name","last_name")

   
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Notification)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)










