from django.db import models

# Create your models here.
class user(models.Model):
    district_id = models.IntegerField()
    email = models.EmailField(max_length=254)
    telegram_sub = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
