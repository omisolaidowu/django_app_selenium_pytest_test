from django.shortcuts import render, get_object_or_404, redirect
from .models import art_gallery
# from .models import category
#from .models import Images
from .forms import my_engine

try:
    from urllib.parse import quote_plus
except:
    pass
#from .forms import ImageForm
from django.contrib.auth.decorators import login_required
from .forms import *
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views import generic
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from comments.forms import commentform 
from django.contrib.contenttypes.models import ContentType
from comments.models import Comment
# Create your views here.


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


"""def enter(request):
	form = my_login()
	if request.method=="POST":
		form    = my_login(request.POST)
		if form.is_valid():
			login.objects.create(**form.cleaned_data)
		form = my_login()
	context ={"form": form}
	return render(request, 'register.html', context)"""

def engine(request, user_id):
    if (request.user.is_staff or request.user.is_superuser):
        # my_list_1=art_gallery.objects.filter(user_id=user_id).order_by('-date_created')

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

"""@login_required
def engine(request):

    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=3)
    if request.method == "POST":
    	postForm = my_engine(request.POST, request.FILES)
    	formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())
    	if postForm.is_valid() and formset.is_valid():
    		post_form = postForm.save(commit=False)
    		post_form.user = request.user
    		post_form.save()
    		for form in formset.cleaned_data:
    			if form:
    				image = form["pictures"]
    				photo = Images(post=post_form, pictures=image)
    				photo.save()
    		return HttpResponseRedirect("/account_view")
    	else:
            print(postForm.errors, formset.errors)
    else:
        postForm = my_engine()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'engine.html',
                  {'postForm': postForm, 'formset': formset})"""






"""class eachpost(DetailView):
    model = art_gallery
    query_pk_and_slug = True
    template = posts.html"""
    

def eachpost(request, slug):
    cat_list_2 = art_gallery.objects.filter(published=True)
    instance = get_object_or_404(art_gallery, slug=slug)
    share_string = quote_plus(instance.content)
    initial_data = {
    "content_type":instance.get_content_type,
    "object_id":instance.id
    }

    form = commentform(request.POST or None, initial=initial_data)
    if form.is_valid():

        
        
        c_type =form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        object_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        parent_obj = None
        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count()==1:
                parent_obj = parent_qs.first()
        new_comment, created = Comment.objects.get_or_create(

            user = request.user,
            content_type = content_type,
            object_id = object_id,
            content = content_data,
            parent = parent_obj,
            )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
        
    comments = instance.comments
    #if each_data != each_data.get_slug():
    if instance.published==True:
        return render(request, 'posts.html', {"instance":instance, "cat_list_2":cat_list_2, "form":form, "comments":comments})
    else:
        if (request.user.is_staff or request.user.is_superuser):
            return render(request, 'posts.html', {"instance":instance, "cat_list_2":cat_list_2, "form":form, "comments":comments})
        else:
            raise Http404

"""class Postlist(generic.ListView):s
    queryset = art_gallery.objects.filter(status=1).order_by('-date_created')
    template_name='engine.html'"""
    
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

