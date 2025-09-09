from django.db import models

# Create your models here.

from django.db import models

class Product(models.Model):
    PRODUCT_CHOICES = [
        ('sepatu', 'Sransfer'),
        ('baju', 'Baju'),
        ('celana', 'Celana'),
        ('raket', 'Raket'),
        ('bola', 'Bola'),
    ]

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    address = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    product = models.CharField(max_length=20, choices=PRODUCT_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    @property
    def is_news_hot(self):
        return self.news_views > 20
        
    def increment_views(self):
        self.news_views += 1
        self.save()
