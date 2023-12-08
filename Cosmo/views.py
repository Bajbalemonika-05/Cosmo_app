from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate,login
from django.contrib.auth import authenticate,login,logout


def home(request):
    return render(request,"Cosmo/index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        Pass1 = request.POST['pass1']
        Pass2= request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request,'Ooopsss! Username already exist! Please try other username.')
            return redirect('signup')

        if User.objects.filter(email=email):
            messages.error(request, 'Email already exist! Please try using another email.')
            return redirect('signup')

        if len(username) > 10:
            messages.error(request,'Username must be 10 characters')
            return redirect('signup')

        if len(Pass1)>=8 :
            messages.error(request,'passowrd must be 8 or less than characters')
            return redirect('signup')

        if Pass1 != Pass2:
            messages.error(request,'passwords did not match!')
            return redirect('signup')

        if not username.isalnum():
            messages.error(request,'username must be Alphanumeric')
            return redirect('signup')

        myuser = User.objects.create_user(username,email, Pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request,"Your Account has been succesfully Created !!")

        return redirect('signin')

    return render(request, "Cosmo/signup.html")

def signin(request):
    if request.method =='POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"Cosmo/index.html",{'fname':fname})
        else:
            messages.error(request,"Wrong Credentials")
            return redirect('signin')

    return render(request,"Cosmo/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"logged Out successfully")
    return render(request,"Cosmo/signout.html")
