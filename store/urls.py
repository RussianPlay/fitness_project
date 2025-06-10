from django.urls import path, include, re_path
from .views import index, product_tab, cart, index_with_order, cart_detail, cart_add, cart_remove, payment
urlpatterns = [
    path('page/', index, name='home'),
    path('page/<int:page>', index, name='move_to_page'),
    path('page/<int:page>/catalog/', index_with_order),  # Без сортировки
    path('page/<int:page>/catalog/<str:sort_command>/', index_with_order),  # С сортировкой
    path('product/<int:product_id>/', product_tab),
    path('payment/', payment),
    
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/page/<int:page>/product/<int:product_id>/', cart_add, name='cart_add'),
    path('cart/remove/product/<int:product_id>/', cart_remove, name='cart_remove'),
]
#'products/<int:productid>/