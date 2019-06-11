from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django import forms


# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category,
                                                      'categories': categories, 'products': products})


def product_detail(request, id, slug, stock):
    category = None
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    cart_product_form.CHOICES = [(i, str(i)) for i in range(1, int(stock)+1)]
    cart_product_form.fields['數量'] = forms.TypedChoiceField(choices=cart_product_form.CHOICES, coerce=int)
    return render(request, 'shop/product/detail.html', {'category': category,
                                                        'categories': categories,
                                                        'product': product,
                                                        'cart_product_form': cart_product_form,
                                                        })

