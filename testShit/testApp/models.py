from django.db import models


# Create your models here.

class Ass(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} {self.address}'


class Master(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Jojo(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    ass = models.ForeignKey(Ass, on_delete=models.CASCADE)
    master = models.ManyToManyField(Master, blank=True, null=True)

    def __str__(self):
        return f'{self.title} - {self.slug}'
