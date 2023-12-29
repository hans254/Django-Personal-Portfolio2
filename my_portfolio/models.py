from django.db import models

# Create your models here.
class Portfolio(models.Model):
    image = models.ImageField(upload_to='my_portfolio/static/images/')
    title = models.CharField('Title', max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True)
