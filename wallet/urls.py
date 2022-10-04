from django.urls import path
from .views import register_Customer
from .views import register_currency
from .views import register_card
from .views import register_wallet
from .views import register_account
from .views import register_notification
from .views import third_party
from .views import register_transactions
from .views import customers_list
from .views import customer_profile


urlpatterns = [
    path("register/", register_Customer, name="transaction"),

    # path("currency/" , register_Currency, name="currency"),
    path("card/", register_card, name="card"),
    path("wallet/", register_wallet, name="wallet"),
    path("account/", register_account, name="account"),
    path("notification/", register_notification, name="notification"),
    path("third_party/", third_party, name="third_party"),
    path("transact/", register_transactions, name="transaction"),
    path("customers/<int:id>/",views.customer_profile,name="customer_profile"),
    path("customers/<int:id>/",views.customer_profile,name="edit_customers"),
    path("customers/", list_customers, name="customers_list")
    # path("currency/", list_customers, name="list_customers"),

]
