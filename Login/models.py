from django.db import models


class Clients(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(
        max_length=128
    )  # You should store hashed/salted passwords
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.username
