from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def get_absolute_url(self):
        return reverse('post_detail', args=[self.pk])


    def __str__(self):
        return self.title