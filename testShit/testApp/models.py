from django.db import models


# Create your models here.

class Ass(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} {self.address}'


class Jojo(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    ass = models.ForeignKey(Ass, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.slug}'
