from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import user, state, district

# Create your views here.
def home(request):
    states = state.objects.all()
    districts = district.objects.all()
    if str(request.user) == 'shivansh':
        if request.method == 'POST':
            userdistrict = request.POST["district_id"]
            email = request.POST["email"]
            telegram = request.POST["telegram"]
            district_id = userdistrict.split(' ')[-1].strip('()')
            createUser = user(email=email, district_id=district_id, telegram_sub=telegram)
            createUser.save()
            return render(request, 'success.html', {'district':district_id, 'email':email, 'telegram':telegram})
        return render(request, 'home.html', {'states': states, 'districts': districts})
    return render(request, 'visitor.html',{'states': states, 'districts': districts})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if str(request.user) == 'shivansh':
                messages.success(request, "Successfully, Logged In.")
                return redirect('admin')
            else:
                messages.error(request, "Not Authorized to Log in, Please try again.")
                return redirect('login')
        else:
            messages.error(request, "Invalid Credentials, Please try again.")
            return redirect('login')
    return render(request, 'login.html')

@login_required
def admin(request):
    if str(request.user) == 'shivansh':
        users = user.objects.all()
        states = state.objects.all()
        districts = district.objects.all()
        if request.method == 'POST':
            userdistrict = request.POST["district_id"]
            is_active = request.POST["is_active"]
            is_telegram = request.POST["is_telegram"]
            telegram_channel_id = request.POST["telegram_channel_id"]
            telegram_channel_name = request.POST["telegram_channel_name"]
            district_id = userdistrict.split(' ')[-1].strip('()')
            updateDistrict = district.objects.get(district_id = district_id)
            updateDistrict.is_active = is_active
            updateDistrict.is_telegram = is_telegram
            updateDistrict.telegram_channel_id = telegram_channel_id
            updateDistrict.telegram_channel_name = telegram_channel_name
            updateDistrict.save()
            return render(request ,'success.html', {'updateDistrict': updateDistrict})
        return render(request, 'admin.html', {'users': users, 'states':states, 'districts': districts})



def logout(request):
    auth.logout(request)
    messages.success(request, "Successfully, Logged Out.")
    return redirect('home')
