from django.db import models
import uuid
from pgvector.django import VectorField

# Create your models here.
class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    content = models.TextField()
    source = models.CharField(max_length=255)
    embedding = VectorField(dimensions=3072,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return super().source
