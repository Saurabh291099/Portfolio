from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def Home_blog(request):
    if request.user.is_authenticated:
        user = User.objects.get(username = request.user)
        context={
        "status":user.is_staff
        }
    else:
        context={
        "status":False
        }


    return render(request,"web_app/blogs_dash/All_blogs.html",context)


def Blog_detail_page(request):
    if request.user.is_authenticated:
        user = User.objects.get(username = request.user)
        context={
        "status":user.is_staff
        }
    else:
        context={
        "status":False
        }
    return render(request,"web_app/blogs_dash/blog_detail.html",context)


def Blog_add_page(request):
    if request.user.is_authenticated:
        user = User.objects.get(username = request.user)
        context={
        "status":user.is_staff
        }
    else:
        context={
        "status":False
        }

    if request.method=="POST":
        title = request.POST['title']
        message = request.POST['message']
        author_by = request.POST['author_by']
        image = request.FILES.get('image')
        feild = request.POST['feild']

        print(title)
        print(author_by)
        print(image)
    return render(request,"web_app/blogs_dash/add_blogs.html",context)