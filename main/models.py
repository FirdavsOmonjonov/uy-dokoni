from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Kategorya")
    slug = models.SlugField(null=True, blank=True, max_length=60, verbose_name="Sulg")

    def __str__(self):
        return self.name

class Home(models.Model):
    title = models.CharField(max_length=50, verbose_name="Sarlavxa")
    description = models.TextField(verbose_name="Batafsil")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    image = models.ImageField(upload_to="home/", verbose_name="Rasm")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategorya")

    def __str__(self):
        return self.title

