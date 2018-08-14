from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.conf import settings
from django.utils import timezone
from .models import Post, Comment, Place
from .forms import PostForm, CommentForm, MapForm
from django.utils.safestring import mark_safe


def post_list(request):
    qs = Post.objects.all().order_by('-created_at')
    # qs = qs.filter(published_date__lte=timezone.now()).order_by('published_date')
    # qs = qs.order_by('published_date')

    return render(request, 'blog/post_list.html', {
        'qs': qs,
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment = Comment.objects.filter(post=pk).order_by('created_at')

    comment_form = CommentForm(request.POST)
    if request.method == 'POST':
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = Post.objects.get(pk=pk)
            comment.save()
            return redirect('post_detail', pk)
        else:
            comment_form = CommentForm(request.POST)

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comment': comment,
        'comment_form': comment_form,
    })

def post_new(request):
    # request.POST (작성 내용/ 필수), request.FILES (이미지, 업로드 파일/ 선택)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.save()
            # return redirect('post_detail', pk=post.pk)
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {
        'form': form,
    })

def post_edit(request, pk):
    # instance 란 행동의 대상을 지정해주는 부분

    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # return redirect('post_detail', pk=post.pk)
            return redirect('post_list')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {
        'form': form,
    })


def map_detail(request):
    map = Place.objects.all()
    counter = len(map)
    empty = []

    for i in range(counter):
        location_split = map[i].location
        foo = location_split.split(',')
        empty.append([map[i].name, float(foo[0]), float(foo[1]), map[i].id])

    return render(request, 'blog/map_detail.html', {
        'empty': mark_safe(empty),
        'GOOGLE_MAP_API': settings.GOOGLE_MAPS_API,
    })


def map_new(request):
    # request.POST (작성 내용/ 필수), request.FILES (이미지, 업로드 파일/ 선택)

    if request.method == 'POST':
        form = MapForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.save()
            # return redirect('post_detail', pk=post.pk)
            return redirect('map_detail')
    else:
        form = MapForm()

    return render(request, 'blog/map_form.html', {
        'form': form,
        'GOOGLE_MAP_API': settings.GOOGLE_MAPS_API,
    })