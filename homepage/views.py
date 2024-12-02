from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
from .models import Thread, Comment, Category
from django.http import HttpResponse
from .forms import ThreadForm


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

def create_thread(request, name):
    category = get_object_or_404(Category, name=name)  # Fetch the category by its name that is passed through previous url

    if request.method == 'POST':
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.created_by = request.user  # Assign the current user as the creator
            thread.category = category  # Automatically set the category
            thread.save()  # Save the thread
            return redirect('home-page')  # Redirect to the home page after successful creation
    else:
        form = ThreadForm()

    return render(request, 'homepage/create_thread.html', {'form': form, 'category': category})

def single_thread(request, slug):
    this_post = get_object_or_404(Thread, slug=slug)
    return render(request, 'homepage/single_post.html',{
    'post': this_post })
