from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import user

# Create your views here.
def home(request):
    if request.method == 'POST':
        district = request.POST["district_id"]
        email = request.POST["email"]
        telegram = request.POST["telegram"]
        createUser = user(email=email, district_id=district, telegram_sub=telegram)
        createUser.save()
        return render(request, 'success.html', {'district':district, 'email':email, 'telegram':telegram})
    return render(request, 'home.html')

@login_required
def register(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Check for errors
        if not username.isalnum():
            messages.error(
                request, "Username must be only letters and numbers.")
            return redirect('register')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if len(password1) < 6:
            messages.error(request, "Password should be greater than 6.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Already Registered. Try logging in")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Already Registered. Try logging in")
            return redirect('register')

        myuser = User.objects.create_user(username, email, password1)
        myuser.save()
        messages.success(request, "Successfully, Registered.")
        return redirect('login')
    if str(request.user) == 'shivansh':
        return render(request, 'register.html')
    return redirect('home')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Successfully, Logged In.")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, Please try again.")
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "Successfully, Logged Out.")
    return redirect('home')
