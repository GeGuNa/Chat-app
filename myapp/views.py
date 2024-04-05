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


def pass_Changing(request):
   if request.user.is_authenticated == False:
      return redirect('/')
      #uups boys 
   
   
   
   from django.contrib import messages
   from django.contrib.auth import login
   
   page = "Authorized/Password.html"
   
   
   kq1_q = request.user
   #Ksus1 = kq1_q.is_authenticated
   #print(kq1_q.check_password("123456"))
   
   if request.method == "POST":
      var_q1 = request.POST.get('npass')
      var_q2 = request.POST.get('opass')
      
      if len(var_q1)<5 or len(var_q2)<5:
         messages.error(request,"Passwords cannot be lesser than 5 symbols")
      elif len(var_q1)>100 or len(var_q2)>100:
         messages.error(request,"Passwords cannot be greather than 100 symbols")
      elif var_q2 == var_q1:
         messages.error(request,"Old password and new password cannot be the same")
      elif request.user.check_password(var_q2) is False:
         messages.error(request,"Old password is incorrect")
      else:
         
         user1 = request.user
         user1.set_password(var_q1)
         user1.save()
         
         login(request, user1)
         
         #vqq_ch = request.user.set_password(var_q1)
         #vqq_ch.save()
         messages.success(request,"Password has been changed")
         
      
   return render(request, page)


def ProfilePic(request):
   from .funcs import handle_uploaded_file
   from django.core.files.storage import FileSystemStorage

   #if request.method == "POST":
      #handle_uploaded_file(request.FILES['fileee'])

   if request.method == 'POST' and request.FILES['Uploaded_File']:
                  ReqFile = request.FILES['Uploaded_File']
                  fs = FileSystemStorage()
                  #fs = FileSystemStorage("myapp/kz1")
                  fs.save(ReqFile.name, ReqFile)
                  #file = fs.save(ReqFile.name, ReqFile)

   return render(request, "file.html")

   


def main(request):
      
   from django.contrib.auth import login, authenticate
   from django.shortcuts import redirect
   
   from .models import Chat 
   import datetime
   
   
   if not request.user.is_authenticated:
      if request.method == "POST":
         usr2 = request.POST['username']
         pass2 = request.POST['password']
         usrent = authenticate(request, username=usr2, password=pass2)
         
         if usrent:
             login(request, usrent)    
             return redirect('/')
         
   
   if request.user.is_authenticated:
      
      ChatQFet = Chat.objects.all()
      
      
      fqFData = {
         'Data': ChatQFet
      }

      mnfil = "Authorized/home.html"
      
      if request.method == "POST":
            rqText = request.POST.get('txt')
            x = datetime.datetime.now()

            KinserTadat = Chat(poster=0,reply=0,text=rqText,post_type="xz",us_id=request.user, when=x)
            KinserTadat.save()
            return redirect('/')
            
            
      return render(request, mnfil, fqFData)
   else:
      return render(request, "home.html")



def signup(request):
   
   from django.contrib.auth.models import User
   from django.contrib.auth import login
   from .models import Accounts
   
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
            
            varq1_qc = Accounts(uid=Kz_usr)
            varq1_qc.save()
            
            
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



from django.contrib.auth.decorators import login_required

@login_required
def change_password(request, new_password):
    user = request.user
    user.set_password(new_password)
    user.save()


@login_required
def change_password_view(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        change_password(request, new_password)
        return HttpResponse('Password changed successfully!')
    else:
        return HttpResponse('Method not allowed.', status=405)




####### login / logout / signup ########

def logout(request):
   from django.contrib.auth import logout
   from django.http import HttpResponse
   #from django.shortcuts import redirect
   logout(request)
   #return HttpResponse("you are out now!")
   return redirect('/')


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
   





