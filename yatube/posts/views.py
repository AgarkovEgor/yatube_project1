from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Group, User
from .forms import PostForm

def paginator_func(post_list,request):
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)


def index(request):
    template = 'posts/index.html'
    post_list = Post.objects.all()
    context = {
        'page_obj': paginator_func(post_list,request=request)
    }
    return render(request, template, context)
def group_posts(request,slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    context = {
        'group': group,
        'page_obj': paginator_func(post_list=posts,request=request)
    }
    return render(request, template, context)

def profile(request, username):
    template_name = 'posts/profile.html'
    author = get_object_or_404(User, username=username)
    posts = author.posts.all()
    context = {
        'author': author,
        'page_obj': paginator_func(post_list=posts,request=request),
    }
    return render(request, template_name, context)


def post_detail(request, post_id):
    template_name = 'posts/post_detail.html'
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post
    }
    return render(request, template_name, context)

@login_required
def post_create(request):
    template_name = 'posts/post_create.html'
    form = PostForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        new_post = form.save(commit=False)
        new_post.author = request.user
        new_post.save()
        return redirect('posts:profile',new_post.author)
    contex = {
        'form': form
    }
    return render(request, template_name, contex)

@login_required
def post_edit(request,post_id):
    template_name = 'posts/post_create.html'
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        return redirect('posts:post_detail', post.id)
    form = PostForm(
        request.POST or None,
        files=request.FILES or None,
        instance=post
        )
    if form.is_valid():
        form.save()
        return redirect('posts:post_detail', post.id)
    context = {
        'form' : form,
        'is_edit': True
    }
    return render(request, template_name, context)


    # Получить пост
    # Проверка автор или нет
    #     Редирект на страницу поста
    # создаем форму
    # Елси валидна
    #     сохраняем изменения
    #     редирект на страницу поста
    # передаем данные с словарь
    # рендер



# Create your views here.
