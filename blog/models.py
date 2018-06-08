import random
from django.db import models
from django.utils import timezone
from django.shortcuts import reverse


def get_random_name():
    foo1 = [
        '배고픈',
        '피곤한',
        '날고싶은',
        '화가난',
        '허리아픈',
        '불쌍한',
        '안심중개사',
        '헛걸음보상제',
        '충성스런',
        '가슴속에사직서를품은',
        '모래반지빵야빵야',
        '요실금걸린',
    ]
    set_foo1 = random.choice(foo1)

    foo2 = [
        'SC',
        'YG',
        '직방',
        '다방',
        '네이버부동산',
        'ZIGBANG',
        '최준호',
        '이의석',
        '강연신',
        '박성환',
        '강연신발닦개',
    ]
    set_foo2 = random.choice(foo2)

    return set_foo1 + ' ' + set_foo2


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