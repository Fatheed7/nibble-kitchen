from django.db import models


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    actioned = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.email
