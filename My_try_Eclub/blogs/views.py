from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from  django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test, login_required

def render_temp_blogs(request):
    context={"is_superuser": False, "user": False,"blogs":[]}

    if user_passes_test(lambda u: u.is_superuser):
        context["is_superuser"]= True
    if request.user.is_authenticated:
        context["user"]=request.user

    for blog in Blog.objects.all():
        context["blogs"].append(blog)

    return render(request, 'blogs.html',context)

#get the notify buttonw working.
#load blogs like we did events in dajango_try. 
#each blog should be a get send to a pk page. (simple like in dajango)
#get the social media links working

def read_blog(request,pk):
    context={"is_superuser": False, "user": False,"blog":None}

    if user_passes_test(lambda u: u.is_superuser):
        context["is_superuser"]= True
    if request.user.is_authenticated:
        context["user"]=request.user #add if the user is the author of the blog in html etc.

    context["blog"]=Blog.objects.get(title=pk) #might change this to UID if needed.

    return render(request, 'read_blog.html',context)

@login_required(login_url='login')
def write_blog(request):
    context={"is_superuser": False, "user": False}

    if user_passes_test(lambda u: u.is_superuser):
        context["is_superuser"]= True
    if request.user.is_authenticated:
        context["user"]=request.user

    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        content = request.POST.get('content')
        author = request.user

        blog = Blog(title=title,desc=desc,content=content,author=author)
        blog.save()

        return redirect('blogs')

    return render(request, 'write_blog.html',context)


@login_required(login_url='login')
def edit_blog(request,pk): 
    context={"is_superuser": False, "user": False,"blog":None}

    if user_passes_test(lambda u: u.is_superuser):
        context["is_superuser"]= True
    if request.user.is_authenticated:
        context["user"]=request.user

    context["blog"]=Blog.objects.get(title=pk) #might change this to UID if needed.
    if context["blog"].author != request.user:
        return redirect('blogs')
    
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        content = request.POST.get('content')
        author = request.user

        context["blog"].title = title
        context["blog"].desc = desc
        context["blog"].content = content
        context["blog"].save()

        return redirect('blogs')

    return render(request, 'edit_blog.html',context)

@user_passes_test(lambda u: u.is_superuser)
def delete_blog(request,pk):
    context={"is_superuser": False, "user": False,"blog":None}

    if user_passes_test(lambda u: u.is_superuser):
        context["is_superuser"]= True
    if request.user.is_authenticated:
        context["user"]=request.user

    context["blog"]=Blog.objects.get(title=pk) #might change this to UID if needed.

    context["blog"].delete()

    return redirect('blogs')