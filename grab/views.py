from django.shortcuts import render,redirect
from grab.forms import *
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, Post,Topic
from .forms import Postform
from django.views import View
from django.utils import timezone
# Create your views here.
# def home(request):
#     posts = Post.objects.all().order_by('-id')
#     topic=Topic.objects.all()
#     context={
#         'posts': posts,
#         'topic':topic
#     }
#     return render(request, 'grab/index.html', context)
def home(request):
    topics = Topic.objects.all()  # Get all topics for rendering buttons
    selected_topic_id = request.GET.get('topic')  # Get selected topic from query parameters
    if selected_topic_id:
        posts = Post.objects.filter(topic_id=selected_topic_id).order_by('-id')
    else:
        posts = Post.objects.all().order_by('-id')
    
    return render(request, "grab/index.html", {
        'posts': posts,
        'topics': topics,
        'selected_topic_id': selected_topic_id
    })
def signup(request):
    form = signupform()
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, "grab/signup.html", {'form': form})

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request, username=name, password=pwd)
            if user is not None:
                login(request, user)
                return redirect('/') 
            else:
                return redirect('login')  
        return render(request, "grab/login.html")
    
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    

def profile(request):
    profiledetails=Post.objects.filter(profile__user=request.user).order_by('-id')
    return render(request,"grab/profile.html",{'profiledetail':profiledetails})
def search_profile(request):
    query_prof = request.GET.get('profile')
    authenticated_user = request.user
    if request.user.is_authenticated:
        results = Profile.objects.exclude(user=authenticated_user)
    else:
        results = Profile.objects.all()
    if query_prof:
        results = Profile.objects.filter(user__username__icontains=query_prof)

    return render(request, 'grab/search.html', {'result': results})

def profile_view(request, id):
    profile = get_object_or_404(Profile, id=id)
    posts = Post.objects.filter(profile=profile)
    context={'profile': profile, 'posts': posts}
    return render(request, 'grab/profileview.html', context)
@login_required
def profile_edit(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if  p_form.is_valid():
            p_form.save()
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form
    }

    return render(request, 'grab/profile_edit.html', context)

def delete(request,id):
    delete_post=Post.objects.get(id=id)
    delete_post.delete()
    return redirect('profile')



def create_post(request):
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = request.user.profile
            post.save()
            return redirect('/')  
    else:
        form = Postform()
    return render(request, 'grab/postform.html', {'form': form})