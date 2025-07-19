from django.shortcuts import render
from .models import Tweet1
from .forms import Tweet1Form, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import SearchForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def tweet_list(request):
   tweets = Tweet1.objects.all().order_by('-created_at')
   return render(request, 'tweet_list.html', {'tweets': tweets})
   

@login_required
def tweet_create(request):
   if request.method == 'POST':
      form = Tweet1Form(request.POST, request.FILES)
      if form.is_valid():
         tweet = form.save(commit=False)
         tweet.user = request.user
         tweet.save()
         return redirect('tweet_list')
   else:
    form = Tweet1Form()
   return render(request, 'tweet_form.html', {'form': form})  
      

@login_required
def tweet_edit(request, tweet_id):
   tweet = get_object_or_404(Tweet1, pk=tweet_id, user = request.user)
   if request.method == 'POST':
       form = Tweet1Form(request.POST, request.FILES, instance=tweet)
       if form.is_valid():
           tweet = form.save(commit=False)
           tweet.user = request.user
           tweet.save()
           return redirect('tweet_list')
   else:
    form = Tweet1Form(instance=tweet)
   return render(request, 'tweet_form.html', {'form': form})  

@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet1, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})

def register(request): 
   if request.method == 'POST':
     form = UserRegistrationForm(request.POST)
     if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()
        login(request, user)
        return redirect('tweet_list')
   else:   
    form = UserRegistrationForm()
   return render(request, 'registration/register.html', {'form': form})

def search_tweets(request):
    form = SearchForm()
    tweets = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            tweets = Tweet1.objects.filter(text__icontains=query).order_by('-created_at')
    return render(request, 'search_results.html', {'form': form, 'results': tweets})
