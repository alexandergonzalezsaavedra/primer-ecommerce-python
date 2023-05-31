from django.urls import re_path
from .views import productListApi,categoryListApi

app_name = 'orders'

urlpatterns = [
    re_path(r"^getproducts$", productListApi.as_view(), name="getproducts"),
    re_path(r"^getcategories$", categoryListApi.as_view(), name="getcategories"),
]