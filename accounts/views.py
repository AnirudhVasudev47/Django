from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse

# Register Here
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            messages.info(request, 'Password does not match.')
            return redirect('register')
        elif User.objects.filter(username = username).exists():
            messages.info(request, 'Username already exists')
            return redirect('register')
        elif User.objects.filter(email = email).exists():
            messages.info(request, 'Email Already exists')
            return redirect('register')
        else:
            user = User.objects.create_user(username = username, first_name = first_name, last_name = last_name, email = email, password = password1)
            user.save()
            print('User created')
            return redirect('login')
        
    else:
        return render(request, 'register.html')

#Login here
def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Wrong Username or Password')
            return redirect('login')

    else:
        return render(request, 'login.html')

#Logout here
def logout(request):
    auth.logout(request)
    return redirect('/')

