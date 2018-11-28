import random
import os
from django.db import models

# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    # print(instance)
    #print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )



class Country(models.Model):
    country_name = models.CharField(max_length=255)

    def __str__(self):
        return self.country_name


class App(models.Model):
    page = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    country = models.ForeignKey(Country)
    currency = models.CharField(max_length=255, choices=(('d','dollar'),('p','pound')))


    def __str__(self):
        return self.page
