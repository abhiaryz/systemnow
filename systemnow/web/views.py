from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import JsonResponse
from .models import Server, Website
# Create your views here.


def login(request):

    if request.method == 'POST':
        username = request['username']
        password = request['password']
        print(username+ "and" + password)
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/base/")
        else:
            messages.info(request, 'invalid credentails')
            return redirect('')
    else:
        return render(request, 'web/login.html')

def register(request):

    if request.method == 'POST':
        first = request.POST['first']
        last = request.POST['last']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already exit')
                return redirect('/register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exist")
                return redirect('/register/')
            else:
                user = User.objects.create_user(first_name=first,last_name=last,username=username, email=email, password=password1)
                user.save();
                return redirect('/login/')
        else:
            messages.info(request, "Password is not matching")
        return redirect('/register/')
    else:
        return render(request, 'web/register.html')


def logout(request):
    auth.logout(request)
    return redirect("/login/")


def index(request):
    return render(request, 'web/index.html')
def ftpserver(request):
    return render(request, 'web/ftpserver.html')
def ftptransfer(request):
    return render(request, 'web/ftptransfer.html')
def linux(request):
    servers = Server.objects.all()
    params = {'server': servers}

    return render(request, 'web/linux.html',params)
def linux2(request):
    return render(request, 'web/linux2.html')
def website(request):
    websites = Website.objects.all()
    naveens = {'website': websites}
    return render(request, 'web/website.html',naveens)

def website_add(request):
        return render(request, 'web/website_add.html')

def server(request):
      return render(request, 'web/server.html')
def server_overview(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        host = request.POST.get('host', '')
        server = Server(name=name, platform=host )
        server.save()
    return render(request, 'web/server_overview.html')
def server_alert(request):
    return render(request, 'web/server_alert.html')
def server_cpu(request):
    return render(request, 'web/server_cpu.html')
def server_incident(request):
    return render(request, 'web/server_incident.html')
def server_memory(request):
    return render(request, 'web/server_memory.html')
def server_from(request):
    return render(request, 'web/server_from.html')
def server_network(request):
    return render(request, 'web/server_network.html')
def server_processes(request):
    return render(request, 'web/server_processes.html')
def server_storage(request):
    return render(request, 'web/server_storage.html')
def website_overview(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        location = request.POST.get('location', '')
        interval = request.POST.get('interval', '')
        url = request.POST.get('url', '')
        print(name, location, interval, url)
        website = Website(name=name, location=location, interval=interval, url=url)
        website.save()
    return render(request,'web/website_overview.html')


def get_data(request):
    ram = {
        "total_ram": 8000,
        "used_ram": 5000,
    }
    return JsonResponse(ram)