from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length= 300)
    logo = models.CharField(max_length= 200)
    slug = models.CharField(max_length= 300)


    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=300)
    category = models.ForeignKey (Category,on_delete=models.CASCADE)
    slug = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Slider(models.Model):
    name = models.CharField(max_length=300)
    image= models.ImageField(upload_to='media')
    description = models.TextField()
    url = models.URLField(max_length = 500,blank = True)

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=300)
    image= models.ImageField(upload_to='media')
    description = models.TextField()
    rank = models.IntegerField()


    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    slug = models.CharField(max_length=300)

    def __str__(self):
        return self.name

STOCK = (('In stock','In stock'),('Out of Stock','Out of stock'))
LABEL = (('new','new'),('sale','sale'),('','default'))

class Product(models.Model):
    name = models.CharField(max_length = 300)
    price = models.IntegerField()
    discounted_price = models.IntegerField(default = 0)
    image = models.ImageField(upload_to='media')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory= models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    brand = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField()
    specification = models.TextField()
    slug = models.TextField()
    stock = models.CharField(max_length=20, choices=STOCK)
    label = models.CharField(max_length=20,choices=LABEL)

    def __str__(self):
        return self.name