from django.db.models import F
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product, Category
from django.views.generic import ListView


def products_home(request):

	cart = request.session.get('cart')
	if not cart:
		request.session['cart'] = {}
    
	products = None
	categories = Category.get_all_categories()
	category_id = request.GET.get('category')
      
	if category_id:
		products = Product.get_all_products_by_category_id(category_id)
	else:
		products = Product.get_all_products().order_by('id')
	
	paginator = Paginator(products, 18)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	
	context = {
        'categories': categories,
        'products': products,
        'page_obj': page_obj,
        'total': len(products),
    }
	return render(request, "products/products.html", context = context)


class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html' 
    context_object_name = 'products'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.get_all_categories()
        return context

    def get_queryset(self):
        filter_option = self.kwargs.get('filter_option')
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

    
