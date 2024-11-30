from django.shortcuts import render
from datetime import date
from django.http import HttpResponse


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

categories = [
    {
        "slug": "gaming",
        "name": "Gaming"
    },
    {
        "slug": "soccer",
        "name": "Football"
    },
    {
        "slug": "ufc",
        "name": "UFC/MMA"
    },
    {
        "slug": "politics",
        "name": "Politics"
    },
    {
        "slug": "housing",
        "name": "Housing"
    },
    {
        "slug": "astronomy",
        "name": "Astronomy"
    },
    {
        "slug": "coding",
        "name": "All things coding"
    },
    {
        "slug": "gastronomy",
        "name": "Cooking fun"
    },
]
# Create your views here.

def get_date(post):
    return post.get("date")

def home(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'homepage/index.html', {
        "categories": categories,
        "posts": latest_posts
    })