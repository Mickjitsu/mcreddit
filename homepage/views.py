from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
from .models import Thread, Comment, Category
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ThreadForm, CommentForm


# Create your views here.

def get_date(post):
    return post.get("date")

def home(request):
    categories = Category.objects.all()
    posts = Thread.objects.all().order_by('-created_at')[:10]
    return render(request, 'homepage/index.html', {
        "categories": categories,
        "posts": posts
    })

def category_threads(request, name):
    categories = Category.objects.all()
    posts = Thread.objects.all()
    this_category = next(cat for cat in categories if cat.name == name)
    relevant_posts = posts.filter(category=this_category)
    return render(request, 'homepage/category.html',{
    'categories': this_category,
    'posts': relevant_posts })

@login_required
def create_thread(request, name):
    category = get_object_or_404(Category, name=name)  # Fetch the category by its name that is passed through previous url

    if request.method == 'POST':
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.created_by = request.user  # Assign the current user as the creator
            thread.category = category  # Automatically set the category
            thread.save()  # Save the thread
            return redirect('pending')  # Redirect to the home page after successful creation
    else:
        form = ThreadForm()

    return render(request, 'homepage/create_thread.html', {'form': form, 'category': category})

def single_thread(request, slug):
    # Get the thread object based on the slug
    this_post = get_object_or_404(Thread, slug=slug)

    # Handle comment submission
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user  # Assign the current user as the comment author
            comment.thread = this_post  # Associate the comment with the current thread
            comment.save()  # Save the comment to the database
            return redirect('single_thread', slug=this_post.slug)  # Redirect back to the thread's page

    else:
        form = CommentForm()

    return render(request, 'homepage/single_post.html', {
        'post': this_post,
        'form': form  # Pass the comment form to the template
    })

def approval(request):
    return render(request, 'homepage/pending_approval.html')
