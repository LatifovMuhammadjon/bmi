from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from expenses.views import ExpenseViewSet, CurrencyViewSet, ExchangeRateViewSet, ExpenseReportView
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view as get_yasg_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet, basename='expense')
router.register(r'currencies', CurrencyViewSet, basename='currency')
router.register(r'exchange-rates', ExchangeRateViewSet, basename='exchange-rate')

schema_view = get_yasg_view(
    openapi.Info(
        title="Wallefy API",
        default_version='v1',
        description="API documentation for the Wallefy application",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/expense-report/', ExpenseReportView.as_view(), name='expense-report'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
