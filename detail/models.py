from django.db import models

# Create your models here.
class Contact_user(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    email=models.EmailField(max_length=200,null=True,blank=True)
    Contact=models.BigIntegerField()
    message=models.CharField(max_length=300,null=True,blank=True)

    def __str__(self):
        return self.name