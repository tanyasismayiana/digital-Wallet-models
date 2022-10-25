from django.shortcuts import render

from .forms import Customer
from .forms import CustomerRegistrationForm
from .forms import CurrencyRegistrationForm
from .forms import CardRegistrationForm
from .forms import WalletRegistrationForm
from .forms import AccountRegistrationForm
from .forms import NotificationRegistrationForm
from .forms import Third_partyRegistrationForm
from .forms import TransactionRegistrationForm
from .forms import LoanRegistrationForm
from django.shortcuts import redirect


def register_customer(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomerRegistrationForm()
        return render(request, 'wallet/register_customer.html',
                      {"form": form})

def list_customers(request):
    customers = Customer.objects.all()
    return render(request, 'wallet/customer_list.html',
                  {"customers": customers})


def customer_profile(request, id):
    customers = Customer.objects.get(id=id)
    return render(request, 'wallet/customer_profile.html',
                  {"customers": customers})


def edit_customer(request, id):
    customer = Customer.objects.get(id=id)
    if request.method == "POST":

        form = CustomerRegistrationForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_profile", id=customer.id)

        else:
            form = CustomerRegistrationForm(instance=customer)
            return render(request, "wallet/edit_customer.html", {"form": form})


def register_currency(request):
    if request.method == "POST":
        form = CurrencyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CurrencyRegistrationForm()
    return render(request, 'wallet/register_currency.html',
                  {"form": form})


def register_card(request):
    form = CardRegistrationForm()
    return render(request, "wallet/register_card.html", {"form": form})


def register_wallet(request):
    form = WalletRegistrationForm()
    return render(request, "wallet/register_wallet.html", {"form": form})


def register_account(request):
    form = AccountRegistrationForm()
    return render(request, "wallet/register_account.html", {"form": form})


def register_notification(request):
    form = NotificationRegistrationForm()
    return render(request, "wallet/register_notification.html", {"form": form})


def third_party(request):
    form = Third_partyRegistrationForm()
    return render(request, "wallet/third_party.html", {"form": form})


def register_transactions(request):
    form = TransactionRegistrationForm()
    return render(request, "wallet/register_transaction.html", {"form": form})


def register_loan(request):
    form = LoanRegistrationForm()
    return render(request, "wallet/register_loan.html", {"form": form})
