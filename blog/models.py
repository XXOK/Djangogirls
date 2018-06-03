import random
from django.db import models
from django.utils import timezone
from django.shortcuts import reverse


def get_random_name():
    foo = [
        '호날두', '메시', '직방', '다방', '호갱노노', '네이버 부동산', '알레스카 김상덕씨', '엄마도 흒댼이야',
    ]
    return random.choice(foo)


class Post(models.Model):
    author = models.CharField(max_length=10, default=get_random_name)
    title = models.CharField(max_length=30, verbose_name='제목', help_text='최대 30 내외')
    text = models.TextField(max_length=300, verbose_name='내용', help_text='최대 300자 내외')
    created_at = models.DateTimeField(
            default=timezone.now)
    published_at = models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def get_absolute_url(self):
        return reverse('post_detail', args=[self.pk])


    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=100, default=get_random_name)
    comment = models.TextField(max_length=100, help_text='최대 100자 내외')
    created_at = models.DateTimeField(auto_now_add=True)