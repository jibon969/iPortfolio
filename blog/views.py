import csv
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib import messages
from .models import (
    Category,
    Blog,
    Comment,
)

from .forms import (
    CategoryForm,
    BlogForm,
    CommentForm,
    ReplyForm
)


def blog(request):
    queryset = Blog.objects.all()
    search = request.GET.get('q')
    if search:
        # Using strip method to remove extra white space
        search = search.strip()
        queryset = Blog.objects.filter(
            Q(title__icontains=search) |
            Q(description=search) |
            Q(title__startswith=search) |
            Q(title__endswith=search)
        ).distinct()
    # Pagination
    paginator = Paginator(queryset, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'object_list': posts,
        'page': page,
        'search': search,
    }
    return render(request, "blog/blog.html", context)


def blog_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    category = get_object_or_404(Category, slug=slug)
    related_post = Blog.objects.filter(category=category)
    comments = post.comments.filter(approve=True)
    new_comment = None

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            messages.add_message(request, messages.SUCCESS, "Comment successfully sent, Thanks")
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'object': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'related_post': related_post,

    }
    return render(request, "blog/blog-details.html", context)
