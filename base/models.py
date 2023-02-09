from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.IntegerField(blank=False)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Person(models.Model):
    username = models.CharField(max_length=20)
    phone_num = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name 
