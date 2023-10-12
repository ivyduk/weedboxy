from django.db import models
from config.mixins import ModelMixin
from apps.packages.models import PackageItem



class Category(ModelMixin):
	name = models.CharField(max_length=50)

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'
  
	@staticmethod
	def get_all_categories():
		return Category.objects.all()
  
	def __str__(self):
		return self.name



class Product(PackageItem):
	image = models.ImageField(upload_to='img/')
	affiliate_url = models.SlugField(blank=True, null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

	def __str__(self):
		return self.name
      

	@staticmethod
	def get_product_by_id(id):
		return Product.objects.get(pk=id)
	
	@staticmethod
	def get_products_by_id(ids):
		return Product.objects.filter(id__in=ids)
  
	@staticmethod
	def get_all_products():
		return Product.objects.all()
  
	@staticmethod
	def get_all_products_by_category_id(category_id):
		if category_id:
			return Product.objects.filter(category=category_id)
		else:
			return Product.get_all_products()
	
	@property
	def discounted_price(self):
		return ((self.price)*(self.discount_percentage))/100 
	
	@property
	def total_price(self):
		return self.price - self.discounted_price if self.has_discount else self.price

	@property
	def has_discount(self):
		return self.discount_percentage > 0

	


