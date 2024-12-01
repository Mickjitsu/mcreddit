from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
from .models import Thread, Comment, Category
from django.http import HttpResponse
from .forms import ThreadForm


all_posts = [
    {
    "slug": "hike-in-the-mountains",
    "image": "mountains.jpg",
    "author": "Mick",
    "date": date(2021, 7, 21),
    "title": "Mountain Hiking",
    "excerpt": "This is gay",
    "content": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Facere possimus at eligendi illum officiis ea ad nemo quis, sunt, vel libero quos laudantium error blanditiis debitis ex amet magni impedit?"
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]


# Create your views here.

def get_date(post):
    return post.get("date")

def home(request):
    categories = Category.objects.all()
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'homepage/index.html', {
        "categories": categories,
        "posts": latest_posts
    })

def category_threads(request, name):
    categories = Category.objects.all()
    this_category = next(cat for cat in categories if cat.name == name)
    return render(request, 'homepage/test.html',{
    'categories': this_category })

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
