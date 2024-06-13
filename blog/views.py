import json

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import CommentForm, ClientInfoForm, CustomUserCreationForm, CreatePost
from blog.models import Blog
from itertools import groupby
from django.utils.timezone import localtime
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.urls import reverse_lazy, reverse


# Login
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True


# Logout
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


# Create your views here.
# @login_required


# @login_required
def create_event_view(request):
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Перенаправление на index после успешного сохранения
    else:
        form = CreatePost()

    return render(request, 'home/create-an-event.html', {'form': form})


def index(request):
    events = Blog.objects.all().order_by('-created')
    return render(request, 'blog/index.html', {'events': events})


def post_detail_view(request, pk):
    event = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/post_detail.html', {'event': event})


# @login_required
def add_comment_to_post(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect('/')
    else:
        form = CommentForm()
    return render(request, 'blog/index.html', context={"form": form})


# class CustomPasswordResetView(PasswordResetView):
#     email_template_name = 'password_reset_done.html'
#     success_url = '/accounts/password_reset/done/'  # URL to redirect after password reset request


def register(request):
    if request.method == 'GET':
        return render(request, 'blog/register.html', {"form": CustomUserCreationForm})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('index'))


def create_post_view(request):
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))  # Замените 'success' на имя URL-шаблона для страницы успеха
    else:
        form = CreatePost()
    return render(request, 'home/create-an-event.html', {'form': form})
