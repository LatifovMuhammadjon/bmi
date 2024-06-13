from rest_framework import serializers
from .models import Expense, Currency, ExchangeRate

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'code', 'name']

class ExchangeRateSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()

    class Meta:
        model = ExchangeRate
        fields = ['id', 'currency', 'rate', 'date']

class ExpenseSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()

    class Meta:
        model = Expense
        fields = ['id', 'user', 'amount', 'category', 'description', 'date', 'currency']
