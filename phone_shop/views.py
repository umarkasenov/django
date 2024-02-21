from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms


def update_phone_view(request, id):
    phone_id = get_object_or_404(models.PhoneShop, id=id)
    if request.method == 'POST':
        form = forms.PhoneShopForm(request.POST, instance=phone_id)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Успешно обновлен в БД</h1> <a href='/'>Все телефоны</a>")
    else:
        form = forms.PhoneShopForm(instance=phone_id)
    return render(request, template_name="phones/update_phone.html",
                  context={"form": form, phone_id: phone_id})

def delete_phone_view(request, id):
    phone_id = get_object_or_404(models.PhoneShop, id=id)
    phone_id.delete()
    return HttpResponse("<h1>Успешно удален из БД</h1> <a href='/'>Все телефоны</a>")



def create_phone_view(request):
    if request.method == 'POST':
        form = forms.PhoneShopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Успешно добавлен в БД</h1> <a href='/'>Все телефоны</a>")
    else:
        form = forms.PhoneShopForm()
    return render(request, template_name="phones/create_phone.html",
                  context={"form": form})


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
