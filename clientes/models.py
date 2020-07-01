from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(decimal_places=2, max_digits=5)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photo', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
