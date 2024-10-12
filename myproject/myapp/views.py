from django.shortcuts import render
from . models import huge
# Create your views here.
def home(request):
    # b=register.objects.all()
    # print(b)
    # return render(request,'home.html',{'det':b})
    return render(request,'home.html')
def about(request):    
    return render(request,'about.html',{})
def menu(request):
    return render(request,'menu.html',{})
def order(request):
    return render(request,'order.html')
def os(request):    
    return render(request,'os.html')
def contact(request):
    return render(request,'contact.html',{})
# def details(request):
#     if request.method=="POST":
#         name1=request.POST["uname"]
#         password1=request.POST["upass"]
#         a=register.objects.create(name=name1,password=password1)
#         return render(request,'os.html')
#     else:
#         return render(request,'register.html')
def wet(request):
    if request.method=="POST":
        coname1=request.POST["coname"]
        name2=request.POST["cname"]    
        email2=request.POST["cmail"]
        quantity2=request.POST["cquan"]
        contact1=request.POST["phno"]
        if coname1 == 'Black Coffee':
            cost2 = int(quantity2 )* 20
        elif coname1 == 'Filter Coffee':
            cost2 = int(quantity2) * 30
        elif coname1 == 'Cappacino':
            cost2 = int(quantity2) * 90
        elif coname1 == 'Americanno':
            cost2 = int(quantity2) * 140
        elif coname1 == 'Esperrsso':
            cost2 = int(quantity2) * 120
        elif coname1 == 'Mocha':
            cost2 = int(quantity2) * 170
        elif coname1 == 'Mochito':
            cost2 = int(quantity2) * 190            
        # cost2=request.POST["cost"]
        b=huge.objects.create( name=name2,email=email2,quantity=quantity2,cost=cost2,contact=contact1,coname=coname1)
        return render(request,'os.html')
def show(request):
    c=huge.objects.all()
    return render(request,'io.html',{'see':c})   