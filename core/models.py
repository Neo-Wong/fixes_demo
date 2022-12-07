from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from . import utils as _u

# Create your models here.


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Products(BaseModel):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='logo')

    def __str__(self):
        return self.name


class Variants(BaseModel):
    name = models.CharField(max_length=63)
    product = models.ForeignKey(to="Products", to_field="id", on_delete=models.DO_NOTHING)
    size = models.CharField(max_length=32, blank=True, null=True)
    color = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.name


class Images(BaseModel):
    Url = models.ImageField(upload_to='image')
    product = models.ForeignKey(to='Products', to_field='id', related_name='product_images', blank=True, null=True, on_delete=models.SET_NULL)  # NOQA E501
    variant = models.ForeignKey(to='Variants', to_field='id', related_name='variant_images', blank=True, null=True, on_delete=models.SET_NULL)  # NOQA E501

    def __str__(self):
        return str(self.id)


@receiver(post_delete)
def delete_file(instance, **kwargs):
    file_path = ''
    if isinstance(instance, Products):
        file_path = instance.logo.path
    if isinstance(instance, Images):
        file_path = instance.Url.path
    _u.delete_upload_file(file_path)
