from django.urls import path
from . import views


urlpatterns = [
    path('', views.phone_shop_view, name="phone_shop"),
    path('phone_detail/<int:id>/', views.phone_shop_detail_view, name="phone_detail"),
]