from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from django.shortcuts import render, redirect

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
   return render(request, "home.html")


def main_of_session(request):
   request.session['cake'] = "lovely"
   #print(request.session)
   #print(request.session['cake'])
   #print('cake' in request.session)
   #print('cake2' in request.session)
   return HttpResponse("hehe")




def kz_file(response):
   #ffl1 = open("files/aba.txt", "rb")
   ffl1 = open("files/right3.jpg", "rb")
   res = FileResponse(ffl1)
   #resp = HttpResponse(response)
   return res
   
