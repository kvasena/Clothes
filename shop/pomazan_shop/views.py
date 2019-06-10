from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from pomazan_shop.forms import ProductForm, SearchProductForm
from pomazan_shop.models import Product


SUCCESS_MESSAGE = u'Товар успешно добален'
ERROR_MESSAGE = u'Поля заполнены не верно'


def index(request):
    return HttpResponse("You're at the index page")


@csrf_protect
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            new_product = Product(
                code=form.cleaned_data['code'],
                gender=form.cleaned_data['gender'],
                colour=form.cleaned_data['colour'],
                size=form.cleaned_data['size']
            )
            new_product.save()
            return render(request,
                          'add_product.html',
                          {'message': SUCCESS_MESSAGE,
                           'products': Product.objects.all().
                                values('id', 'code',
                                            'gender', 'colour',
                                            'size', 'date_of_sale',
                                            'created_on')})
        return render(request,
                      'add_product.html', {'message': ERROR_MESSAGE})
    return render(request, 'add_product.html')


def search_product(request, ):
    if request.method == 'POST':
        form = SearchProductForm(request.POST)
        if form.is_valid():
            return render(request,
                          'search_product.html',
                          {'products': Product.objects.filter(code=form.cleaned_data['code']).
                            values('id', 'code', 'gender', 'colour',
                                   'size', 'date_of_sale', 'created_on')})
        else:
            return render(request,
                          'search_product.html', {'message': ERROR_MESSAGE})
    else:
        return render(request, 'search_product.html')
