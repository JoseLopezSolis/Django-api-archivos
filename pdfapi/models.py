from django.db import models

# Create your models here.
class Crudpdf(models.Model):
  file = models.FileField(upload_to='uploads/')
  filename = models.CharField(max_length=50, null=True)
  upload_date = models.DateTimeField(auto_now_add=True)


