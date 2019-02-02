from django.db import models

# Create your models here.
class user(models.Model):
    auth_user=models.TextField()

    def __str__(self, ):
        return 'user #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'users'


class Entry(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self, ):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'posts'
