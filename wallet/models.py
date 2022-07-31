from datetime import datetime
from email.policy import default
from locale import currency
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    gender = models.CharField
    address = models.TextField
    email = models.EmailField
    phoneNumber = models.CharField(max_length=10)
    age = models.SmallIntegerField
    profile_picture = models.ImageField
    pin = models.IntegerField
    # nationality = models.Charfield(max_length=15)
    marital_status = models.CharField(max_length=10)
    signature = models.ImageField
    employment_status = models.CharField
    id_Number = models.IntegerField


class Wallet(models.Model):
    Balance = models.IntegerField
    customer = models.OneToOneField
    pin = models.SmallIntegerField
    currency = models.ForeignKey
    active = models.BooleanField
    date_created = models.DateTimeField(default=datetime)
    type = models.CharField(max_length=15)


class Account(models.Model):
    attribute = models.CharField(max_length=15)
    account_type = models.CharField(max_length=10)
    account_name = models.CharField(max_length=15)
    savings = models.IntegerField
    wallet = models.ForeignObject
    destination = models.CharField(max_length=15)


class Notification(models.Model):
    Unique_identifier = models.CharField(max_length=15)
    # Sent_on = models.DatetimeField(default = datetime.now,auto_now = False)
    # Received_at = models.DatetimeField(default = datetime.now,auto_now = False)
    # Delivered_on = models.DatetimeField()
    Message = models.TextField


class Transaction(models.Model):
    transaction_type = models.CharField(max_length=15)
    account_origin = models.CharField
    destination = models.CharField
    third_Party = models.ForeignObject
    dateTime = models.DateTimeField
    receipt = models.CharField(max_length=15)
    status = models.CharField(max_length=10)


class Card(models.Model):
    date_Issued = models.DateTimeField
    card_status = models.CharField
    # security_code = models.smallpositiveIntegerField()
    signature = models.ImageField
    issuer = models.CharField
    account = models.ForeignKey
    expiry_date = models.DateField(default=datetime)
    card_name = models.CharField
    card_type = models.CharField


class Receipt(models.Model):
    date = models.DateTimeField(default= datetime.now,auto_now=False)
    transaction = models.ForeignKey
    receipt_file = models.FileField


class Loan(models.Model):
    loan_type = models.CharField
    amount = models.IntegerField
    wallet = models.ForeignKey
    date_time = models.DateTimeField(default= datetime.now,auto_now=False)
    loan_terms = models.CharField
    payment_dueDate = models.DateTimeField(default= datetime.now,auto_now=False)
    guaranter = models.CharField
    balance = models.CharField
    duration = models.CharField
    interest_rate = models.IntegerField
    stutus = models.CharField


class Reward(models.Model):
    wallet = models.ForeignKey
    points = models.IntegerField
    date = models.ForeignKey
    transaction = models.ForeignKey
