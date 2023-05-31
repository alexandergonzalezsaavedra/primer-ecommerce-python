from django.urls import re_path
from .views import productListApi

app_name = 'orders'

urlpatterns = [
    re_path(r"^getproducts$", productListApi.as_view(), name="getproducts"),
]