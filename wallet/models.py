
from django.utils import timezone
from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=10,null=True)
    last_name = models.CharField(max_length=10,null=True)
    gender = models.CharField(max_length=10,null=True)
    address = models.TextField()
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=14,null=True)
    age = models.SmallIntegerField()
    profile_picture = models.ImageField(upload_to='profile_picture/',null=True)
    pin = models.IntegerField()
    # nationality = models.Charfield(max_length=24)
    marital_status = models.CharField(max_length=10,null=True)
    signature = models.ImageField()
    employment_status = models.CharField(max_length=10,null=True)
    id_Number = models.IntegerField()


class Currency (models.Model):
    amount = models.PositiveBigIntegerField()
    symbol = models.CharField(max_length=15, null=True)
    country = models.CharField(max_length=24, null=True)


class Card(models.Model):
    date_Issued = models.DateField(default=timezone.now)
    card_status = models.CharField(max_length=24,null=True)
    # security_code = models.smallpositiveIntegerField()
    signature = models.ImageField()
    issuer = models.CharField(max_length=24,null=True)
    expiry_date = models.DateField(default=timezone.now)
    card_name = models.CharField(max_length=24,null=True)
    card_type = models.CharField(max_length=24,null=True)
    
class Wallet(models.Model):
    Balance = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='Wallet_customer')
    pin = models.SmallIntegerField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE,related_name='Wallet_currency')
    active = models.BooleanField()
    date_created = models.DateField(default=timezone.now)
    type = models.CharField(max_length=24,null=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE,related_name='Wallet_card')


class Account(models.Model):
    account_type = models.CharField(max_length=10,null=True)
    account_name = models.CharField(max_length=25,null=True)
    savings = models.IntegerField()
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE,related_name='Account_wallet')
    destination = models.CharField(max_length=30,null=True)
    card = models.OneToOneField(Card, on_delete=models.CASCADE,related_name='Account_card')
    



class Notification(models.Model):
    Unique_identifier = models.CharField(max_length=24,null=True)
    Sent_on = models.DateField(default=timezone.now)
    Received_at = models.DateField(default=timezone.now)
    Delivered_on = models.DateField(default=timezone.now)
    Message = models.TextField()


class Third_party(models.Model):
    full_name = models.CharField(max_length=15, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15,null=True)
    transaction_cost = models.IntegerField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    status = models.BooleanField()


class Transaction(models.Model):
    transaction_type = models.CharField(max_length=24,null=True)
    account_origin = models.CharField(max_length=24,null=True)
    destination = models.CharField(max_length=25,null=True)
    third_Party = models.ForeignKey(Third_party, on_delete=models.CASCADE,related_name='Transaction_third_party')
    dateTime = models.DateField(default=timezone.now)
    status = models.CharField(max_length=24,null=True)


class Receipt(models.Model):
    date = models.DateField(default=timezone.now)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE,related_name='Receipt_transaction')
    receipt_file = models.FileField(upload_to='wallet/')





class Loan(models.Model):
    loan_type = models.CharField(max_length=24,null=True)
    amount = models.IntegerField()
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE,related_name='Loan_wallet')
    date_time = models.DateField(default=timezone.now)
    loan_terms = models.CharField(max_length=24,null=True)
    payment_dueDate = models.DateField(default=timezone.now)
    guaranter = models.CharField(max_length=24,null=True)
    balance = models.CharField(max_length=24,null=True)
    duration = models.CharField(max_length=24,null=True)
    interest_rate = models.IntegerField()
    stutus = models.CharField(max_length=24,null=True)


class Reward(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE,related_name='Reward_wallet')
    points = models.IntegerField()
    date = models.DateField(default=timezone.now)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE,related_name='Reward_transaction')
