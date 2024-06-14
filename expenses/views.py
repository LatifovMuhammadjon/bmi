from rest_framework import viewsets
from .models import Expense, Currency, ExchangeRate
from .serializers import ExpenseSerializer, CurrencySerializer, ExchangeRateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from datetime import date


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [IsAuthenticated]


class ExchangeRateViewSet(viewsets.ModelViewSet):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer
    permission_classes = [IsAuthenticated]


class ExpenseReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        expenses = Expense.objects.filter(user=user)
        report = expenses.values('currency__code').annotate(
            total_amount=Sum('amount'))


        today = date.today()
        for item in report:
            currency_code = item['currency__code']
            rate = ExchangeRate.objects.filter(
                currency__code=currency_code, date=today).first()
            if rate:
                item['rate'] = rate.rate
                item['total_amount_base_currency'] = item['total_amount'] * rate.rate
            else:
                item['rate'] = None
                item['total_amount_base_currency'] = None

        return Response(report)
