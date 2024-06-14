from django.contrib import admin
from .models import Expense, Currency, ExchangeRate

admin.site.register(Expense)
admin.site.register(Currency)
admin.site.register(ExchangeRate)