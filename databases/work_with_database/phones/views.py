from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    sort = request.GET.get('sort')
    if sort == 'name':
        phones = Phone.objects.order_by('name')
    elif sort == 'price-min':
        phones = Phone.objects.order_by('price')
    elif sort == 'price-max':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()
    context = {'phones': phones}
    template = 'catalog.html'
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
