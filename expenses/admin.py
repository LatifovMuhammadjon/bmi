from django.contrib import admin
from .models import Expense, Currency, ExchangeRate
from django.contrib.admin import AdminSite
admin.site.register(Expense)
admin.site.register(Currency)
admin.site.register(ExchangeRate)


class MyAdminSite(AdminSite):
    site_header = 'Wallefy Administration'
    site_title = 'Wallefy Admin'
    index_title = 'Welcome to Wallefy Admin'