from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField('Название', max_length=100)
    slug = models.SlugField('Слаг', max_length=100, editable=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Category: {self.name}>"


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    name = models.CharField('Название', max_length=100)
    category = models.ManyToManyField(Category, verbose_name='Категории', related_name='products')
    slug = models.SlugField('Слаг', max_length=100, editable=False)
    price = models.DecimalField('Цена', max_digits=20, decimal_places=2)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Product: {self.name}>"


class ProductImage(models.Model):
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField("Изображение", upload_to='images', height_field='height', width_field='width')
    height = models.PositiveIntegerField("Длина", editable=False)
    width = models.PositiveIntegerField("Высота", editable=False)

    def __str__(self):
        return self.product.name

    def __repr__(self):
        return f"<ProductImage: {self.product.name}>"
