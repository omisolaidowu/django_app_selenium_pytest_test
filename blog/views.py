from django.shortcuts import render, get_object_or_404, redirect
from .models import art_gallery
from .forms import my_engine

try:
    from urllib.parse import quote_plus
except:
    pass
from .forms import *

from django.contrib import messages
from django.http import HttpResponseRedirect, Http404

from django.shortcuts import redirect

from django.contrib.auth.models import auth
from django.core.paginator import Paginator
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


def catlist(request):
    cat_list = art_gallery.objects.filter(published=True)
    return render(request, 'catlist.html', {"cat_list":cat_list})

def home(request):
    data_1 = art_gallery.objects.all()
    data = art_gallery.objects.filter(published=True).order_by('-date_created')
    p = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    return render(request, 'home.html',  {"page_obj":page_obj, "data_1":data_1})



def engine(request, user_id):
    if (request.user.is_staff or request.user.is_superuser):
        

        if request.method=="POST":
            form = my_engine(request.POST or None, request.FILES or None)
            if form.is_valid():
                post_form = form.save(commit=False)
                post_form.user = request.user

            post_form.save()
            return HttpResponseRedirect("/")
        else:
            postForm = my_engine()
            context = {"postForm":postForm}
    else:
        raise Http404
        
    return render(request, 'engine.html', context)


def login(request):
    
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if (request.user.is_staff or request.user.is_superuser):
                return HttpResponseRedirect("/engine/{user_id}".format(user_id= user.id))
            else:
                return HttpResponseRedirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/login')
    

def eachpost(request, slug):
    cat_list_2 = art_gallery.objects.filter(published=True)
    instance = get_object_or_404(art_gallery, slug=slug)
    share_string = quote_plus(instance.content)
    initial_data = {
    "content_type":instance.get_content_type,
    "object_id":instance.id
    }

    if instance.published==True:
        return render(request, 'posts.html', {"instance":instance})
    else:
        if (request.user.is_staff or request.user.is_superuser):
            return render(request, 'posts.html', {"instance":instance})
        else:
            raise Http404
    
def postlist(request):
    if request.user.is_superuser:
        queryset=art_gallery.objects.all().order_by('-date_created')
    else:
        return Http404
    return render(request, 'postlist.html', {"queryset":queryset})

def userlist(request, user_id):
    my_list=art_gallery.objects.filter(user_id=user_id)
    return render(request, 'userlist.html', {"my_list":my_list})

def edit_post(request, pk, user_id):
    if (request.user.is_staff or request.user.is_superuser):
        p_list=art_gallery.objects.filter(user_id=user_id).order_by('-date_created')

            
        post = get_object_or_404(art_gallery, pk=pk, user_id=user_id)
        if post.user==request.user:
            if request.method == 'POST':
                form = my_engine(request.POST, request.FILES, instance=post)
                if form.is_valid():
                    form.save()
                    
                    return HttpResponseRedirect("/")
                
                else:
                    form = my_engine(instance=post)
            else:
                form = my_engine(instance=post)
        else:
            raise Http404
    else:
        raise Http404
    return render(request, 'edit.html', {'form':form, 'post':post, 'p_list':p_list})

def delete_post(request, pk):
    if request.user.is_superuser:
        obj = get_object_or_404(art_gallery, pk=pk)
        if request.method=="POST":
            obj.delete()
            return redirect('/postlist')
    else:
        raise Http404
    return render(request, 'delete.html', {"obj":obj})

