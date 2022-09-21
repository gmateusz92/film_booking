from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from movie_admin.models import MovieMaster

def home(request):
    return render(request, 'home.html', {})

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists(): #sprwdza czy uzytkownik nie jest juz w bazie danych
                messages.error(request, 'Username already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password) #first_name dlatego ze w postgre w kolumnie jest first_name
                    auth.login(request, user) #po stworzeniu konta zutomatycznie loguje
                    messages.success(request, 'You are now logged in')
                    return redirect('home')
                    user.save()
                    messages.success(request, 'You are registered successfully')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
        #messages.error(request, 'This is error message') # w static/js/ app js dodaje funkcje settimeOut (potem komenda python manage.py collectstatic) (aby message znikalapo paru sekundach) jak nie dziala w zrodle strony szukam app.js i odswiezam
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('home')
        else:
            messages.error(request,'Invalid login credentials')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)

        return redirect('home')
    return redirect('home')

def dashboard(request):
    movies = MovieMaster.objects.all().filter()
    return render(request, 'dashboarda.html', {'movies': movies})

def buyticket(request):
    return render(request, 'buyticket.html')


def bookticket(request):
    return render(request, 'bookticket.html')