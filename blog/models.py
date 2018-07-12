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
        '배부른',
        '활기찬',
        '축구선수',
        '농구선수',
        '야구선수',
        '배구선수',
        '요리왕',
        '설명충',
        '가능충',
    ]
    set_foo1 = random.choice(foo1)

    foo2 = [
        '이무송',
        '김인직',
        '김행직',
        '김참직',
        '감스트',
        '이점덕',
        '김순덕',
        '김말자',
        '박막례',
        '이춘자',
        '박술녀',
        '표인봉',
        '고인물',
    ]
    set_foo2 = random.choice(foo2)

    return set_foo1 + ' ' + set_foo2


class Post(models.Model):
    author = models.CharField(
        max_length=20, default=get_random_name)
    title = models.CharField(
        max_length=30, verbose_name='제목')
    text = models.TextField(
        max_length=300, verbose_name='내용', blank=True, null=True)
    photo = models.ImageField(
        max_length=300, verbose_name='이미지', upload_to='upload_img', blank=True
    )
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
    comment = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)