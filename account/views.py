from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.shortcuts import redirect

def login(request):
    if request.method == "GET": # USUARIO ESTA APENAS ACESSANDO A PAGINA
        if request.user.is_authenticated: # VERIFICA SE O USUARIO ESTA AUTENTICADO
            return redirect('/')
        else:
            return render(request , 'login.html')
        
    if request.method == "POST": # USUARIO ESTA FAZENDO LOGIN
        username = request.POST.get('username')
        password = request.POST.get('password')

        login_user = authenticate(username=username , password=password)

        if login_user is not None:
            login_django(request , login_user)
            return redirect('/')
        else: # Implementar sistema de senha incorreta
            print("Problemas no login")
            return render(request , 'login.html' , {"response":"Usuário ou Senha incorretos"})
    

def register(request):
    if request.method == "GET": # USUARIO ESTA APENAS ACESSANDO A PAGINA
        if request.user.is_authenticated: # VERIFICA SE O USUARIO ESTA AUTENTICADO
            return redirect('/')
        else:
            return render(request , 'register.html' , {'user_exists':False} )
        
    if request.method == "POST": # USUARIO ESTA SE CADASTRANDO
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')        

        check_username = User.objects.filter(username = username).first()
        if check_username :
            return render(request , 'register.html' , {'user_exists':True})
        else:
            new_user = User.objects.create_user(
                username= username,
                email=email,
                password=password
            )
            new_user.save()
            return redirect('login')
        

def profile(request):
    if request.user.is_authenticated:
        username = request.user.username
        print(username)
        return render(request , 'profile.html' , {'username':username})
    else:
        return redirect('login')


def logout(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            logout_django(request)
            return redirect('login')
        else:
            return redirect('/')