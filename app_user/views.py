from django.shortcuts import render,redirect
from app_user.forms import Usersignup,Userlogin
from django.contrib import messages
from app_user.models import Userlogintable
from app_admin.models import Movietable
from django.core.paginator import Paginator

def signuppage(request):
    return render(request,"app_user/usersignup.html",{"forms":Usersignup})

def savesignup(request):
    x=request.POST.get("username")
    y=request.POST.get("pas")
    #print(x)
    #print(y)
    us=Usersignup(request.POST)
    if us.is_valid():
        us.save()
        Userlogintable(usrname=x, pas=y).save()
        messages.success(request,"SignUp Successfully")
        return redirect("signuppage")
    else:
        messages.error(request,"Invalid Details")
        return redirect("signuppage")

def userlogin(request):
    return render(request,"app_user/userlogin.html",{"forms":Userlogin})

def userloginhome(request):
    n = request.POST.get("usrname")
    a = request.POST.get("pas")
    try:
        Userlogintable.objects.get(usrname=n, pas=a)
        x = Movietable.objects.all()
        p = Paginator(x, 3)
        page_no = request.GET.get("pno")
        if page_no:
            page = p.page(page_no)
        else:
            page = p.page(1)
        return render(request, "app_user/userpage.html", {"data": page,"name":n})

    except Userlogintable.DoesNotExist:
        messages.error(request, "Invalid User")
        return redirect("userlogin")

def searchaction(request):
    x=request.POST.get("s1")
    try:
        Movietable.objects.get(moviename=x)
        res = Movietable.objects.filter(moviename=x)
        a=Movietable.objects.values('moviename')
        #print(a)
        return render(request,"app_user/searchpage.html",{"data":res})
    except Movietable.DoesNotExist:
        messages.error(request,"Not Found")
        return render(request,"app_user/searchpage.html",{"msg":messages})