from django.db.models.deletion import CASCADE
from djongo import models

# Create your models here.
class user(models.Model):
    district_id = models.IntegerField()
    email = models.EmailField(max_length=254)
    telegram_sub = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "user"

class state(models.Model):
    _id = models.ObjectIdField()
    state_id = models.IntegerField(unique=True)
    state_name = models.TextField()
    class Meta:
        db_table = "states"

class district(models.Model):
    _id = models.ObjectIdField()
    is_active = models.BooleanField()
    is_telegram = models.BooleanField()
    district_id = models.IntegerField()
    district_name = models.TextField()
    telegram_channel_name = models.TextField(default= '')
    telegram_channel_id = models.TextField(default= '')
    # state_id = models.ForeignObject(to=state, on_delete=models.CASCADE, from_fields=['state_id'], to_fields=['_id'])

    class Meta:
        db_table = "districts"
