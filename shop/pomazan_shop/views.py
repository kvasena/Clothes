from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from pomazan_shop.forms import ProductForm
from pomazan_shop.models import Product



SUCCESS_MESSAGE = u'Товар успешно добален'


def index(request):
    return HttpResponse("You're at the index page")


@csrf_protect
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            new_product = Product(
                code=form.cleaned_data['code'],
                gender=form.cleaned_data['gender'],
                colour=form.cleaned_data['colour'],
                size=form.cleaned_data['size']
            )
            new_product.save()
            return render(request,
                          'add_product.html', {'success': SUCCESS_MESSAGE})
    return render(request, 'add_product.html')


def search_product(request):
    return render(request, 'search_product.html')
