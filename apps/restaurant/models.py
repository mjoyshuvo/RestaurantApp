from django.db import models
from conf.validators import validate_file_extension_menu
from datetime import date


class BaseModel(models.Model):
    created_at = models.DateField(default=date.today)
    updated_at = models.DateField(default=date.today)

    class Meta:
        abstract = True


class Restaurant(BaseModel):
    name = models.CharField(null=False, blank=False, unique=True, max_length=30)


class Menu(BaseModel):
    restaurant = models.ForeignKey(Restaurant, null=False, blank=False, on_delete=models.CASCADE,
                                   related_name='restaurant')
    menu = models.FileField(upload_to='menus', null=False, blank=False, validators=[validate_file_extension_menu])
    vote_count = models.IntegerField(null=False, blank=False, default=0)

    class Meta:
        unique_together = ('restaurant', 'created_at')


class Result(BaseModel):
    restaurant = models.ForeignKey(Restaurant, null=False, blank=False, on_delete=models.CASCADE,
                                   related_name='result_restaurant')

    class Meta:
        unique_together = ('restaurant', 'created_at')

    def __str__(self):
        return self.pk
