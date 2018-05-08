from django.db import models

# Create your models here.


class Animal(models.Model):

    name = models.CharField(max_length=60)
    sound = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animals"

    def speak(self):
        return 'The %s says \"%s\"' % (self.name, self.sound)

    def __str__(self):
        return self.name
