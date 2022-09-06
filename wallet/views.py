from django.shortcuts import render
from .forms import CustomerRegistrationForm
from .forms import CurrencyRegistrationForm
from .forms import CardRegistrationForm
from .forms import WalletRegistrationForm
from .forms import AccountRegistrationForm
from .forms import NotificationRegistrationForm
from .forms import Third_partyRegistrationForm
from .forms import TransactionRegistrationForm
from .forms import LoanRegistrationForm


# Create your views here.
# read about hhtp contex

def register_customer(request):
    form = CustomerRegistrationForm()
    return render(request, "wallet/register_customer.html",{"form":form})

def register_currency(request):
    form = CurrencyRegistrationForm()
    return render(request, "wallet/register_currency.html",{"form":form})

def register_card(request):
    form = CardRegistrationForm()
    return render(request, "wallet/register_card.html",{"form":form})

def register_wallet(request):
    form = WalletRegistrationForm()
    return render(request, "wallet/register_wallet.html",{"form":form})

def register_account(request):
    form = AccountRegistrationForm()
    return render(request, "wallet/register_account.html",{"form":form})  

def register_notification(request):
    form = NotificationRegistrationForm()
    return render(request, "wallet/register_notification.html",{"form":form})      

def third_party(request):
    form = Third_partyRegistrationForm()
    return render(request, "wallet/third_party.html",{"form":form})   


def register_transactions(request):
    form = TransactionRegistrationForm()
    return render(request, "wallet/third_party.html",{"form":form})

def register_loan(request):
    form = LoanRegistrationForm()
    return render(request, "wallet/third_party.html",{"form":form})