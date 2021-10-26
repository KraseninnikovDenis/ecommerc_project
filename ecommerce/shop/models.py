from django.db import models

class Category (models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name='название категории')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='слаг')
    discription= models.TextField(blank=True, verbose_name='описание категории')
    image= models.ImageField(upload_to='category', blank=True, verbose_name='картинка')

    class Meta:
        #ordering=('name')
        verbose_name='категория'
        verbose_name_plural='категории'


    def __str__(self):
        return self.name

class Product (models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name='название продукта')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='слаг')
    discription= models.TextField(blank=True, verbose_name='описание продукта')
    image= models.ImageField(upload_to='product', blank=True, verbose_name='картинка продукта')
    category=models.ForeignKey(Category,on_delete=models.CASCADE, verbose_name='категория')
    price=models.DecimalField(max_digits=10,decimal_places=2, verbose_name='цена продукта')
    stok=models.IntegerField(verbose_name='количество продукта')
    available=models.BooleanField(default=True, verbose_name='наличие продукта продукта')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        #ordering=('name')
        verbose_name='продукт'
        verbose_name_plural='продукты'
   
    def __str__(self):
        return self.name