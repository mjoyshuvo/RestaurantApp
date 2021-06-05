from django.db import models


class Restaurant(models.Model):
    name = models.CharField(null=False, blank=False, unique=True, max_length=30)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, null=False, blank=False, on_delete=models.CASCADE,
                                   related_name='restaurant')
    menu = models.FileField(upload_to='menus', null=False, blank=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('restaurant', 'created_at')