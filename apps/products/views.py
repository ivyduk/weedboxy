from django.db.models import F, ExpressionWrapper, FloatField
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product, Category
from django.views.generic import ListView



def products_home(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}

    products = Product.get_all_products().order_by('id')
    categories = Category.get_all_categories()
    
    
 
    filter_option = request.GET.get('filter_option')

    if filter_option == 'recent':
        products = products.order_by('-created_at')[:16]
    elif filter_option == 'promo': 
        products = Product.get_products_with_discount().order_by('-discount_percentage')

         

    paginator = Paginator(products, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'products': products,
        'page_obj': page_obj,
        'total': len(products),
        'selected_filter_option': filter_option, 
    }
    return render(request, "products/products.html", context=context)



class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html' 
    context_object_name = 'products'
    paginate_by = 8
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        context['category_id'] = category_id 
        context['categories'] = Category.get_all_categories()
        return context


    def get_queryset(self):
        filter_option = self.request.GET.get('filter_option')
        category_id = self.kwargs.get('category_id')
        products = Product.objects.all()

        if category_id:
            products = products.filter(category=category_id)

        if filter_option == 'recent':
            products = products.order_by('-created_at')
        elif filter_option == 'promo':
            products = products.filter(discount_percentage__gt=0).annotate(
                discounted_price=F('price') - F('price') * F('discount_percentage') / 100
            ).order_by('discounted_price')

        return products
    


def product_search(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Product.objects.filter(name__icontains=query)

    categories = Category.get_all_categories()

    products = results

    paginator = Paginator(products, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'page_obj': page_obj,
        'total': len(products),
        'results': results,
        'query': query
    }

    return render(request, 'products/product_search.html', context)





  
