from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        text = f'{self.name} at {self.timestamp.strftime("%B-%d-%Y")}'
        return text

    class Meta:
        ordering = ('-timestamp',)
