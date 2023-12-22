from django.db import models

class Category(models.Model):
    ''' Model for a category '''

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    
    def __str__(self):
        ''' Returns the categories name as a string '''
        return self.name

    
    def get_friendly_name(self):
        ''' Returns the user-friendly name as a string '''
        return self.friendly_name



class Product(models.Model):
    ''' Model for a product '''
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


def __str__(self):
    ''' Returns the products name as a string '''
    return self.name



