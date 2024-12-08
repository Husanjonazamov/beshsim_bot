from django.db import models


    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Sim(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos')
    category = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.name


# Create your models here.
class PhoneNumber(models.Model):
    number = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    
    company = models.ForeignKey(Sim, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.number