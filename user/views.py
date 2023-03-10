from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from user.models import Contact,Menu,Gallery,Chef


# Create your views here.

#=======index view======================

def home(request):
    return render(request, "home.html")


#=======about view========================

def about(request):
    return render(request, "others/about.html")

#==========menu view===========================

def menu(request):
    dish=Menu.objects.all()
    context={'data': dish}
    return render(request, "others/menu.html", context)

#=======chefs view===========================


def chefs(request):
    chef = Chef.objects.all()
    context = {'data': chef}
    return render(request, "others/chefs.html", context)

#========gallery view==========================


def gallery(request):
    view = Gallery.objects.all()
    context = {'data': view}
    return render(request, "others/gallery.html", context)


#=========contact view=============================



def contact_us(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        desc=request.POST.get('desc')
        query= Contact(name=name,email=email,phonenumber=number,description=desc)
        query.save()

        messages.info(request, 'Thanks for Contacting us we will get back you soon')
        return redirect('/contact')

    return render(request, "others/contact.html")





#============login view===============================
def handlelogin(request):
    if request.method == 'POST':
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request, 'Login successfully')
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/login')
            
    return render(request, 'user/login.html')

#============logout view ===============================

def handlelogout(request):
    logout(request)
    messages.success(request, 'Logout success')
    return redirect('/login')


#================register view=================================

def register(request):
    if request.method == 'POST':
        username=request.POST.get('usernumber')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        if len(username)>11 or len(username)<11:
            messages.info(request, 'Phone number must be 11 digits')
            return redirect('/register')

        if pass1 != pass2:
            messages.info(request, 'Password is not Matching')
            return redirect('/register')
        
        try:
            if User.objects.get(username=username):
                messages.warning(request, 'Phone number is Taken')
                return redirect('/register')

        except Exception as identifier:
            pass

                
        try:
            if User.objects.get(email=email):
                messages.warning(request, 'email is Taken')
                return redirect('/register')

        except Exception as identifier:
            pass

        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,'User is created please login')
        return redirect('/login')

    return render(request, 'user/register.html')