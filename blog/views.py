from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm


def post_list(request):
    qs = Post.objects.all()
    # qs = qs.filter(published_date__lte=timezone.now()).order_by('published_date')
    # qs = qs.order_by('published_date')

    return render(request, 'blog/post_list.html', {
        'post_list': qs,
    })

def post_detail(request, detail_pk):
    post = get_object_or_404(Post, pk=detail_pk)
    return render(request, 'blog/post_detail.html', {
        'detail': post,
    })

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })