from django.db.models.signals import pre_save
from django.dispatch import receiver

from market.utils import slugify_unicode
from products.models import Category
from products.models import Product


@receiver(pre_save, sender=Category, weak=False)
def on_category_edit(instance, **_):
    instance.slug = slugify_unicode(instance.name)


@receiver(pre_save, sender=Product, weak=False)
def on_product_edit(instance, **_):
    instance.slug = slugify_unicode(instance.name)
