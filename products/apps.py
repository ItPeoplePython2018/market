from django.apps import AppConfig


class ProductsConfig(AppConfig):
    name = 'products'
    verbose_name = 'Каталог продукции'

    def ready(self):
        import products.handlers    # used: !!
