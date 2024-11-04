from django.db import models

class BaseModel(models.model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_add=True)
    
    class Meta:
        abstract = True