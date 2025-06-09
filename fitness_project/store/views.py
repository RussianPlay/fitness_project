from django.shortcuts import render, redirect, get_object_or_404
from .models import Products, Category
from django.http import HttpResponse
from django.views import  View
from .cart import Cart
from django.http import HttpResponseRedirect
# Create your views here.
PRODUCT_CARDS_NUMBER_PER_PAGE = 20

def index(request, page=1):
    if request.method == 'GET':
        recommended_data = Products.get_recommended_products()
        product_data = Products.get_products_page(page)
        sz = Products.get_size()
        mx_page = sz // PRODUCT_CARDS_NUMBER_PER_PAGE + (1 if sz % PRODUCT_CARDS_NUMBER_PER_PAGE else 0)
        end_page = min(page + 4, mx_page)
        if end_page < 4:
            start_page = 1
        elif end_page - page < 4:
            start_page = end_page - 4
        else:
            start_page = page
        return render(request, 'store/index.html', context={
            'product_data':product_data,
            'recommended_data':recommended_data,
            'page':page,
            'start_page':start_page,
            'end_page':end_page,
            'mx_page':mx_page,
            'prange' : range(start_page, end_page + 1),
            'en_rus_catalog': Category.en_rus_catalog,
                                                    })

def index_with_order(request, page = 1, sort_command = ''):
    product_data = Products.get_products_page(page_number=page, sort_command=sort_command)
    sz = Products.get_size()
    mx_page = sz // PRODUCT_CARDS_NUMBER_PER_PAGE + (1 if sz % PRODUCT_CARDS_NUMBER_PER_PAGE else 0)
    end_page = min(page + 4, mx_page)
    if end_page < 4:
        start_page = 1
    elif end_page - page < 4:
        start_page = end_page - 4
    else:
        start_page = page

    cont = {
        'product_data':product_data,
        'rus_version':Category.en_rus_catalog.get(sort_command, sort_command),
        'page':page,
        'start_page':start_page,
        'end_page':end_page,
        'mx_page':mx_page,
        'sort_command':sort_command,
        'PRODUCT_CARDS_NUMBER_PER_PAGE':PRODUCT_CARDS_NUMBER_PER_PAGE
    }
    return render(request, "store/sorted_index.html", context=cont)


def product_tab(request, product_id):
    prod = Products.get_products_by_id([product_id])[0]
    return render(request, 'store/product_tab.html', context={'product_item':prod})


def cart_add(request,  product_id = 1):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    cart.add(product)
    # return redirect('move_to_page', page=page)\
    pivot = request.GET.get('pivot', 'ERROR')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/') + f"#{pivot}")

def cart_decrease(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    cart.decrease(product)
    pivot = request.GET.get('pivot', 'ERROR')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/') + f"#{pivot}")

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'store/cart.html', {'cart': cart})


def cart(request):
    cart_data = Products.get_products_page(page_number=1)
    return render(request, 'store/cart.html', context={'cart_data':cart_data, 'en_rus_catalog' : Category.en_rus_catalog})
