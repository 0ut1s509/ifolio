from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from folio.utils import kreye_slug
import random
# Create your models here.

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    non = models.CharField(max_length=100)
    siyati = models.CharField(max_length=100)
    imel = models.EmailField(max_length=200)
    foto = models.ImageField(upload_to = 'profile_foto/', blank = True, null = True)
    telefon = models.CharField(max_length=100)

    def __str__(self):
        return self.non


class Project(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tit = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 200, blank=True)
    dat_kreye = models.DateField(auto_now_add = True)
    deskripsyon = models.CharField(max_length = 400)
    foto = models.ImageField(upload_to = 'projet_foto/', blank = True, null = True)

    categorys = models.ManyToManyField('Category', blank = True)

    def __str__(self):
        return self.tit



    def save(self, *args, **kwargs):
        if self.pk is None:
                self.slug = kreye_slug(self,field_name='tit')
        super(Project, self).save(*args, **kwargs)


class Category(models.Model):
    chwa = (('design', 'DESIGN'), ('food','FOOD'), ('education','EDUCATION'), ('energy','ENERGY'), ('technology','TECHNOLOGIE'), ('programming','PROGRAMMING'), ('health',' HEALTH'), ('finance','FINANCE'), ('money','MONEY'))

    non = models.CharField(max_length = 50, choices=chwa)

    def __str__(self):
        return self.non