from django.db import models

class jobs(models.Model):
  
    image=models.ImageField(upload_to='media')

    text=models.CharField(max_length=200)
    def __str__(self):
        return self.text

