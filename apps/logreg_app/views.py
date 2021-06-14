from django.shortcuts import render, redirect
from .models import User
from ..ideas_app.models import Idea
from .forms.register import RegisterForm
from .forms.login import LoginForm
from django.db.models import Count
import bcrypt

# Create your views here.
def home(request):
    ideas_ordered = Idea.objects.annotate(count = Count('likes')).order_by('-count')
    context = {
        'ideas': ideas_ordered
    }
    return render(request, 'home.html', context)

def logreg(request):
    #cuando la la solicitud es GET
    if request.method == 'GET':
        reg_form = RegisterForm()
        login_form = LoginForm()
        #si no hay un usuario en session, hacer el render
        if 'user_id' not in request.session:
            return render(request, 'logreg.html', {'reg_form': reg_form, 'login_form': login_form})
        #si ya hay un usuario en session, redirigir a ideas brillantes
        else:
            return redirect('/ideas_brillantes')
    
    #cuando la solicitud es POST
    elif request.method == 'POST':
        #si el form es el de registro, validar, registrar y agregar a session
        if request.POST['form_to_post'] == 'register':
            reg_form = RegisterForm(request.POST)
            login_form = LoginForm()
            if reg_form.is_valid():
                pw = request.POST['password']
                pw_hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()
                User.objects.create(
                    name = request.POST['name'],
                    alias = request.POST['alias'],
                    email = request.POST['email'],
                    password = pw_hash
                )
                user = User.objects.last()
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                request.session['user_alias'] = user.alias
                return redirect('/ideas_brillantes')
            else:
                return render(request, 'logreg.html', {'reg_form': reg_form, 'login_form': login_form})
        #si el form es de login, validar, login y agregar a session
        if request.POST['form_to_post'] == 'login':
            print('estoy en login')
            login_form = LoginForm(request.POST)
            reg_form = RegisterForm()
            try:
                if login_form.is_valid():
                    print('login form es valido')
                    user = login_form.login(request.POST)
                    if user:
                        request.session['user_id'] = user.id
                        request.session['user_name'] = user.name
                        request.session['user_alias'] = user.alias
                        return redirect('/ideas_brillantes')
                    
                else:
                    message_error = "Usuario y/o contraseña incorrecto"
                    return render(request, 'logreg.html', {'reg_form': reg_form, 'login_form': login_form, 'msg_login_error': message_error})
            except:
                print('loginform not valid')
                message_error = "Usuario y/o contraseña incorrecto"
                return render(request, 'logreg.html', {'reg_form': reg_form, 'login_form': login_form, 'msg_login_error': message_error})

def logout(request):
    request.session.flush()
    return redirect('/')

def user(request, user_id):
    #try:
        user_selected = User.objects.get(id = int(user_id))
        ideas = user_selected.ideas.all().count()
        likes = user_selected.ideas_liked.all().count()
        print(ideas)
        print(likes)
        context = {
            'user_selected': user_selected,
            'ideas': ideas,
            'likes': likes
        }
        return render(request, 'user.html', context)
    #except:
    #    return redirect('/ideas_brillantes')