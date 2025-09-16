from django.db import models
import uuid

# Create your models here.

from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('sepatu', 'Sepatu'),
        ('baju', 'Baju'),
        ('celana', 'Celana'),
        ('raket', 'Raket'),
        ('bola', 'Bola'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='baju')
    product_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    def increment_views(self):
        self.product_views += 1
        self.save()
