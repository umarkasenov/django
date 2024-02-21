from django.urls import path
from . import views


urlpatterns = [
    path('', views.phone_shop_view, name="phone_shop"),
    path('phone_detail/<int:id>/', views.phone_shop_detail_view, name="phone_detail"),
    path('phone_detail/<int:id>/delete/', views.delete_phone_view, name="phone_delete"),
    path('phone_detail/<int:id>/update/', views.update_phone_view, name="update_phone"),
    path('create_phone/', views.create_phone_view, name="create_phone"),
]