from django.shortcuts import render, get_object_or_404
from . import models


def phone_shop_view(request):
    if request.method == 'GET':
        phone = models.PhoneShop.objects.all()
        return render(request, template_name='phones/phone_list.html',
                      context={'phone': phone})


def phone_shop_detail_view(request, id):
    if request.method == 'GET':
        phone_id = get_object_or_404(models.PhoneShop, id=id)
        return render(request, template_name='phones/phone_detail.html',
                      context={'phone_id': phone_id})
