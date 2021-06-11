from django.db import models
from django.urls import reverse


# Home task 9. Model Person
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    def get_absolute_url(self):
        """Returns the url to access a particular person instance."""
        return reverse('update-person', args=[str(self.pk)])
