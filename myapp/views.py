from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from django.shortcuts import render, redirect

#from myapp.models import Accounts
from .models import Accounts


# Create your views here.


def main(request):
   print(f" from main {request.session['xz']}")
   return HttpResponse("hehe")

def main_test(request, test: str):
   return HttpResponse(f"hehe {test}")


def main_test2(request):
   aba = {
      "horrendous":"123456"
   }
   return render(request, "aba.html", aba)
   #return HttpResponse("qqqqqq")



def Main_pg2(request):
   #qz1 = Accounts.objects.get(id=1)
   #print(qz1.name)
   #print(qz1.surn)
   print(" user ", request.user.is_authenticated)
   return render(request, "home.html")


def main_of_session(request):
   request.session['cake'] = "lovely"
   #print(request.session)
   #print(request.session['cake'])
   #print('cake' in request.session)
   #print('cake2' in request.session)
   return HttpResponse("hehe")


####### login / logout / signup ########

def logout(request):
   from django.contrib.auth import logout
   from django.http import HttpResponse
   logout(request)
   return HttpResponse("you are out now!")


def login(request):
   from django.contrib.auth import login, authenticate
   from django.http import HttpResponse
   from django.shortcuts import redirect


   usr2 = 'Phantom'
   pass2 = '123456'
   usrent = authenticate(request, username=usr2, password=pass2)
   
   if usrent:
       login(request, usrent)    
       return redirect('/')
   else:
       print(f"is credentials {request.user.is_authenticated}")
       return HttpResponse(f"nope {request.user.is_authenticated}")




#####################

def kz_file(response):
   #ffl1 = open("files/aba.txt", "rb")
   ffl1 = open("files/right3.jpg", "rb")
   res = FileResponse(ffl1)
   #resp = HttpResponse(response)
   return res
   





