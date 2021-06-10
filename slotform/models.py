from djongo import models

# Create your models here.
class user(models.Model):
    district_id = models.IntegerField()
    email = models.EmailField(max_length=254)
    telegram_sub = models.BooleanField(default=False)
    time = models.TimeField(auto_now= True)
