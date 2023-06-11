from django.urls import re_path
from .views import categoryListApi,subcategoryListApi,productListApi

app_name = 'orders'

urlpatterns = [
    re_path(r"^getcategories$", categoryListApi.as_view(), name="getcategories"),
    re_path(r"^getsubcategories$", subcategoryListApi.as_view(), name="getsubcategories"),
    re_path(r"^getproducts$", productListApi.as_view(), name="getproducts"),
]