from django.shortcuts import render
from gym.models import Activity
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponseRedirect
from gym.forms import contactForm
from django.core.mail import EmailMessage 

# Create your views here.

def index(request):
    return render(request, 'index.html')

def activity(request):
    activities = Activity.objects.all()
    return render(request, 'activity.html', {'activities': activities})

def consult_activities(request):
    if "search" in request.GET and request.GET["search"]:
        consult= request.GET ["search"] 
        activities = Activity.objects.filter(type__contains=consult) 
        return render(request, 'result.html', {'activities': activities})
    else:
        return render(request, 'result.html')


def new_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        try:
            form.save()
            return render(request, 'created_user.html')
        except:
            return render(request, 'new_user.html', {'form': form}) 
        
    else:
        form= UserCreationForm()
        return render(request, 'new_user.html', {'form': form})

def enter(request):
    if not request.user.is_anonymous: 
        return HttpResponseRedirect("/private")
    elif request.method == "POST":
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            user = request.POST["username"]
            password = request.POST["password"] 
            access = authenticate(username=user, password=password)
            if access is not None: 
                if access.is_active:
                    login(request, access)
                    return HttpResponseRedirect('/private')
            else:
                return render(request, 'no_user.html')
    else: 
        form = AuthenticationForm()
        return render(request, 'enter.html', {'form': form})

@login_required(login_url='/enter')
def private(request): 
    user = request.user
    return render(request, 'private.html', {'user': user})

def exit(request):
    if not request.user.is_anonymous:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def contact(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            title = 'Correo desde del gimnasio'
            content = form.cleaned_data['message'] + '\n\n'
            content += 'Comunicarse al correo:'+ form.cleaned_data['email']
            email = EmailMessage(title, content, to = ["gimnasiolasmaravillas@gmai.com"])
            try: 
                email.send()
                return render(request, "email_sent.html")
            except: 
                return render(request, "email_no_sent.html")
    else:
        form = contactForm()
        return render(request, 'contact.html', {"form": form})

def error_404(request, exception):    
    return render(request, '404.html', {})

def error_500(request):
    return render(request, '500.html', {})
