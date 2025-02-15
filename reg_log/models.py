from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30) 
    email = models.EmailField(max_length=100, unique=True)
    age = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']    

    def __str__(self):
        return self.first_name
    
class UserWeight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user} - {self.weight} - {self.date}'