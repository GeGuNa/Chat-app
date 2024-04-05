def handle_uploaded_file(f):   
    with open('myapp/static/'+f.name, 'wb+') as destination:   
        for chunk in f.chunks(): 
            destination.write(chunk)  


def UnixTime():
   pass
   
   
def Random_integer():
   
   from random import randint
   
   num1 = randint(0, 9)
   num2 = [1,2,3,4,5,6,7,8,9,10]
   num3 = randint(1, 100)
   
   
   return  num2[num1]*num3


#print(Random())
