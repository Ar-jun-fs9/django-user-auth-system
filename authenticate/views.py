from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout



# Create your views here.
def index(request):
     if request.user.is_authenticated:
        # User is logged in
        return render(request, "index.html", {"message": request.user.username})

     else:
        # User is anonymous
     #    message = "Welcome, anonymous user!"
       return redirect("loginUser")

     

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print (username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Login successful
            return redirect("index")
        else:
            # Login failed
            return render(request, "login.html", {"error": "Invalid credentials"})
    
    return render(request, "login.html")

def logoutUser(request):
     logout(request)
     return redirect("loginUser")