from django.urls import path
from .views import register_customer
from .views import register_currency
from .views import register_card
from .views import register_wallet
from .views import register_account
from .views import register_notification
from .views import third_party


urlpatterns = [
    path("register/", register_customer, name="customer")
    path("currency/", register_currency.html, name="currency"),
    path("card/", register_card.html, name="card"),
    path("wallet/", register_wallet.html, name="wallet"),
    path("account/", register_account.html, name="account"),
    path("notification/", register_notification.html, name="notification"),
    path("third_party/", third_party.html, name="third_party")

]
