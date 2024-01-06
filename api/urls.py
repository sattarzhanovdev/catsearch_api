from django.urls import path
from .views import get_binance_prices, get_bybit_prices, get_okx_prices, get_all_prices, get_crypto_prices, get_binance_price_dynamic, get_bybit_price_dynamic, get_okx_price_dynamic, getUSDTsFirst, getUSDTsSecond, getUSDTsThird, getUSDTsFourth

urlpatterns = [
  path('api/binance/', get_binance_prices),
  path('api/bybit/', get_bybit_prices),
  path('api/okx/', get_okx_prices),
  path('api/all/', get_all_prices),
  path('api/prices/', get_crypto_prices),
  path('api/binance/<str:symbol>/', get_binance_price_dynamic),
  path('api/bybit/<str:symbol>/', get_bybit_price_dynamic),
  path('api/okx/<str:symbol>/', get_okx_price_dynamic),
  path('api/auto/1/', getUSDTsFirst),
  path('api/auto/2/', getUSDTsSecond),
  path('api/auto/3/', getUSDTsThird),
  path('api/auto/4/', getUSDTsFourth),
]
