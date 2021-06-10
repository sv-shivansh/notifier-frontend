from django.shortcuts import render
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