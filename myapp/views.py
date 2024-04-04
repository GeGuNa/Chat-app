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



def main(request):
      
   from django.contrib.auth import login, authenticate
   from django.shortcuts import redirect

   if not request.user.is_authenticated:
      if request.method == "POST":
         usr2 = request.POST['username']
         pass2 = request.POST['password']
         usrent = authenticate(request, username=usr2, password=pass2)
         
         if usrent:
             login(request, usrent)    
             return redirect('/')
         
   
   if request.user.is_authenticated:
      mnfil = "Authorized/home.html"
   else:
      mnfil = "home.html"
   
   return render(request, mnfil)



def signup(request):
   
   from django.contrib.auth.models import User
   from django.contrib.auth import login
   
   
   print(" user ", request.user.is_authenticated)
   
   if request.user.is_authenticated:
      return redirect("/")
   
   if request.method == "POST":
       v_usr = request.POST['username']
      
       try:
            Kz_usr1 = User.objects.get(username=v_usr)
       except User.DoesNotExist:  

            v_usrpass = request.POST['password']
            v_usremail =  request.POST['email']
            
            print(f"  usr  {v_usr}")
            
            Kz_usr = User.objects.create_user(v_usr, v_usremail, v_usrpass)
            Kz_usr.save()
            
            login(request, Kz_usr)
            
            #now we can redirect user to main page
            return redirect("/")
      
   return render(request, "signup.html")




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
   





