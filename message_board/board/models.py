from django.db import models

# Create your models here.
from django.db import models

class Message(models.Model):
    text = models.TextField()
    source = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)

