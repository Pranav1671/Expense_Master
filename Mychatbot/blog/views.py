from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import UserProfile
from .models import UserProfile1
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
# Create your views here.

from .forms import UserProfileForm

def create_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('open_html')  # Replace 'success_url' with your success page URL
        else:
            return render(request, 'blog/profilepage.html', {'error': 'Invalid name or password'})
    else:
        form = UserProfileForm()
    
    return render(request, 'open_html', {'form': form})

def openweb(request):
    return render(request, 'blog/myweb.html')

def my_expense_view(request):
    return render(request, 'blog/web2.html')

def open_html(request):
    return render(request, 'blog/profilepage.html')


from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile1

def save_user_profile(request):
    if request.method == 'POST':
        # Fetch the user profile based on the unique name
        name = request.POST.get('name')
        user_profile = get_object_or_404(UserProfile1, name=name)
        
        # Update the user profile fields with the form data
        user_profile.logpass = request.POST.get('password')
        
        # Save the updated user profile
        user_profile.save()
        
        # Redirect to 'openweb' after saving
        return redirect('openweb')
    
    return render(request, 'blog/login.html')

    

def open_login(request):
    return render(request, 'blog/login.html')

def open_signup(request):
    return render(request, 'blog/signup.html')


def loginpass(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('logpass')

        if name == 'pranav' and password == '123456':
            return redirect('openweb')
        else:
            return render(request, 'blog/login.html', {'error': 'Invalid name or password'})
    
    return render(request, 'blog/login.html')

def signuppass(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('logpass')
        phone = request.POST.get('phone')
        return render(request, 'blog/login.html', {'error': 'Under Development'})   
    return render(request, 'blog/login.html')