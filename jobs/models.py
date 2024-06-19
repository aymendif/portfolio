from django.db import models

class connect_db (models.Model):
  
    image=models.ImageField(upload_to='images/')

    text=models.CharField(max_length=200)
